twitcher.controller('TimelineCtrl', ['$scope', '$rootScope', 'TimelineResource',
    function ($scope, $rootScope, Timeline) {
        $scope.timeline = [];

        $scope.processEntities = function(tweet) {
            var find, replace;
            var mentions = tweet.entities.user_mentions;
            var medias = tweet.entities.media;
            var hashtags = tweet.entities.hashtags;
            var urls = tweet.entities.urls;
            var tweet = tweet.text;

            // Links to mentions
            if (mentions !== undefined)
            angular.forEach(mentions, function(mention) {
                find = '@' + mention.screen_name;
                replace = '<a href="http://twitter.com/' + find + '">' + find + '</a>';
                tweet = tweet.replace(find, replace);
            });

            // Links to urls
            if (urls !== undefined)
            angular.forEach(urls, function(url){
                find = url.url;
                replace = '<a href="' + url.url + '">' + url.display_url + '</a>';
                tweet = tweet.replace(find, replace);
            });

            // Media to urls (photos to img)
            if (medias !== undefined)
            angular.forEach(medias, function(media){
                find = media.url;
                replace = '<a href="' + media.media_url + '">' + media.display_url + '</a>';

                if (media.type === 'photo') {
                    replace = '<img class="photo" src="' + media.media_url + '">';
                }
                tweet = tweet.replace(find, replace);
            });

            // Hashtags to urls
            if (hashtags !== undefined)
            angular.forEach(hashtags, function(hashtag){
                find = '#' + hashtag.text;
                replace = '<a href="https://twitter.com/hashtag/' + hashtag.text + '">#' + hashtag.text + '</a>';
                tweet = tweet.replace(find, replace);
            });

            return tweet;
        };

        $scope.getTimeline = function () {
            var screenName = $scope.screen_name ? $scope.screen_name.replace('@', '') : 'bit2pixel';
            Timeline.query({
                screen_name: screenName,
                count: 10
            }, function (data) {
                $scope.timeline = data;
                $scope.user = data[0] && data[0].user;

                if ($scope.user !== undefined) {
                    $rootScope.backgroundColor = $scope.user.profile_background_color;
                    $rootScope.backgroundImage = $scope.user.profile_banner_url;
                    $rootScope.linkColor = $scope.user.profile_link_color;
                    $rootScope.textColor = $scope.user.profile_text_color;
                }
            });
        };

        $scope.$watch('screen_name', function(){
            $scope.getTimeline();
        });
    }
]);