$(document).ready(function() {
    $( "select[name=month]" ).val( "{{ month_text }}" );
    $('select[name=month]').change(function () {
    console.log($('select[name=month]').val());
    month = $('select[name=month]').val();
    $('.form').submit();
});
});