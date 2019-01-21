function getRandomIdea() {
    $.ajax({
        url: 'random/',
        type: 'get',
        success: function(data) {
            $('#randomIdeaContent').html(data);
        },
        failure: function(data) {
            $('#randomIdeaContent').html(data);
        }
    });
}