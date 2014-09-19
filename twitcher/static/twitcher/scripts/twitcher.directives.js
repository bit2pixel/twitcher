twitcher.directive('fadeImage', function() {
    return {
        link: function(scope, element) {
            element.on('load', function() {
                element.addClass('fade-in');
            });
        }
    };
});