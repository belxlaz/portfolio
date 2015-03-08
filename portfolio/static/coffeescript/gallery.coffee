$ ->

  # enable filter
  $('.filter').find('li').click ->

    # toggle filter menu class
    $(this).parent().find('li').removeClass 'active'
    $(this).addClass 'active'

    # get keywords
    keywords = $(this).attr('data-keywords').split /\s*,\s*/
    
    # hide all projects
    $('.gallery').fadeOut {
      complete: ->
        
        # filter
        $(this).find('li').each ->
          classes = $(this).attr('class').split ' '
          intersection = array_intersection keywords, classes
          if intersection.length then $(this).show() else $(this).hide()
  
        # show gallery
        $(this).fadeIn()
    }

array_intersection = (a, b) ->
  $.grep a, (i) ->
    $.inArray(i, b) > -1
