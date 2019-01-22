var allowed = true;

function getRandomIdea() {
    if (allowed) {
        loadIdeaData();
        allowed = false;
        allowTimeOut()
    }
}

function allowTimeOut() {
    setTimeout(function() { allowed = true; }, 10000);
}

function loadIdeaData() {
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