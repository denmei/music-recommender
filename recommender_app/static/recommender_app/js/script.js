$(document).ready(function() {

    $("#submit").click(function(event) {

        var uInput = $("#inputartist").val();
        var predictUrl = $("#inputartist").attr("response-url");

        var val = $.ajax({
                url: predictUrl,
                dataType: 'application/json',
                type: 'POST',
                data: JSON.stringify({artist: uInput, number: 5}),
                success: function(response) {
                    alert(response);
                },
                error: function(xhr, ajaxOptions, thrownError) {
                    console.log("g");
                    console.log(xhr.responseJSON);
                    alert(xhr.responseJSON);

                }
             })
    });
});