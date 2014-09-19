twitcher.factory('TimelineResource', function ($resource) {
    return $resource('/api/1/timeline/:screen_name.json', {
        screen_name: '@screen_name'
    }, {
        get: {
            method: 'GET'
        }
    })
});