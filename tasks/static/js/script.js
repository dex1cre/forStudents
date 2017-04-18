function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(function() {
  $('.click_ask').click(function() {
    $(this).addClass('active');
    var csrf_token = getCookie('csrftoken');
    if ($(this).prev('input').val() != "" &&
        $(this).prev('input').prev('input').val() != "")
        $.ajax({
          url: '/subject/',
          type: 'POST',
          data: {
            ask: $(this).prev('input').prev('input').val(),
            id: $(this).prev('input').val()
          },
          beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
          },
          success: function(data) {
            if (data == "okay") {
              $('.active').next('.ask_result').addClass('succes_ask');
              $('.active').next('.ask_result').text('Правильно!)))');
            } else {
              $('.active').next('.ask_result').addClass('bad_ask');
              $('.active').next('.ask_result').text(data);
            }
          }
        });
    else
      alert("Сначала впишите ответ!")
  });

  $('.next_task').click(function() {
    $(this).parents('.task').remove();
  });
});
