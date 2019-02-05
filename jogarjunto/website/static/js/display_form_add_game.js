$(document).ready(function() {
    $('#online_true').focus(function() {
        $('div.what_game').show();
        $('input.game_online').show();
        $('label.game_online').show();
        $('div.url_game').show();
        $('input.game_offline').hide();
        $('label.game_offline').hide();
        $('div.address_game').hide();
    });

    $('#online_false').focus(function() {
        $('div.what_game').show();
        $('input.game_offline').show();
        $('label.game_offline').show();
        $('div.address_game').show();
        $('input.game_online').hide();
        $('label.game_online').hide();
        $('div.url_game').hide();
    });


    $('div.what_game').hide();
    $('input.game_online').hide();
    $('label.game_online').hide();
    $('input.game_offline').hide();
    $('label.game_offline').hide();
    $('div.url_game').hide();
    $('div.address_game').hide();
});
