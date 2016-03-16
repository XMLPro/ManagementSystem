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
        $(".tag-item-group").on("click", ".glyphicon-remove", function () {
            var remove_form = $(this).parents('.ajax_remove');
            $.ajax({
                url: remove_form.prop('action'),
                type: "POST",
                dataType: 'json',
                data: {
                    'tag_id': $(this).parent().next(".tag_id").val()
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
            var event_tag = $(this);
            var t_input = event_tag.parents('.input-group').find('.tag-input');
            var arr = t_input.val().split(/\s+/);
            $.ajax({
                url: event_tag.parents('.tag-edit').find('.ajax_post').prop('action'),
                type: "POST",
                dataType: 'json',
                data: {
                    'text': t_input.val(),
                    'equipment_id': event_tag.parents('.input-group').find('.equipment_id').val()
                },
                'success': function (response) {
                    console.log(response.tags_id);
                    console.log(response.tags_id[0]);
                    for (var i = 0; i < arr.length; i++) {
                        event_tag.parents('li').find('.tag-item-group').append(
                            "<span class='tag-item'>" +
                            "<span class='label label-primary'>" + arr[i] + "</span>" +
                            "<span class='glyphicon glyphicon-remove' aria-hidden='true'></span>" +
                            "</span>" +
                            "<input type='hidden' name='tag_id' class='tag_id' value=" + response.tags_id[i] + ">"
                        );
                        event_tag.parents('li').find('.glyphicon-remove').show();
                    }
                }
            });
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