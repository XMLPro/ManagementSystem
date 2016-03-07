/**
 * Created by Owner on 2016/03/04.
 */
$(function () {
        $(".edit-show").on("click", function () {
            var text = $(this).text();
            if (text === "タグ編集") {
                $(this).text("タグ編集完了")
            } else {
                $(this).text("タグ編集")
            }
            $(this).parents().children(".tag-edit").toggle(200);
            $(this).parents("li").find(".glyphicon-remove").toggle();
        });

        //タグの削除部分
        $(".glyphicon-remove").on("click", function () {
            var remove_form = $(this).parents('.ajax_remove');
            $.ajax({
                url: remove_form.prop('action'),
                type: "POST",
                dataType: 'json',
                data: {
                    'tag_id': remove_form.children(".tag_id").val()
                }
            });
            $(this).parents('.tag-item').remove();

        });
        $(".ajax_post").submit(function (event) {
            event.preventDefault();
            $(this).find(".tag-submit").trigger("click");
        });

        //タグの追加に関しての部分
        $(".tag-submit").on("click", function () {
            var t_input = $(this).parents('.input-group').find('.tag-input');
            var arr = t_input.val().split(/\s+/);
            for (var i = 0; i < arr.length; i++) {
                $(this).parents('li').find('.ajax_remove').append("<span class='tag-item'>" +
                    "<span class='label label-primary'>" + arr[i] + "</span>" +
                    "<span class='glyphicon glyphicon-remove' aria-hidden='true'></span>" +
                    "</span>");
                $(this).parents('li').find('.glyphicon-remove').show();
            }
            $.ajax({
                url: $(this).parents('.tag-edit').find('.ajax_post').prop('action'),
                type: "POST",
                dataType: 'json',
                data: {
                    'text': t_input.val(),
                    'equipment_id': $(this).parents('.input-group').find('.equipment_id').val()
                }
            })
        });


        jQuery(document).ajaxSend(function (event, xhr, settings) {
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

            function sameOrigin(url) {
                // url could be relative or scheme relative or absolute
                var host = document.location.host; // host + port
                var protocol = document.location.protocol;
                var sr_origin = '//' + host;
                var origin = protocol + sr_origin;
                // Allow absolute or scheme relative URLs to same origin
                return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                        // or any other URL that isn't scheme relative or absolute i.e relative.
                    !(/^(\/\/|http:|https:).*/.test(url));
            }

            function safeMethod(method) {
                return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
            }

            if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        });
    }
);