$ ->

  # save the initial status of the gallery
  $.projects = $('.gallery').clone()

  # enable filter
  $('.filter').find('li').click ->

    # toggle class
    $(this).parent().find('li').removeClass 'active'
    $(this).addClass 'active'

    # get keywords
    keywords = $(this).attr('data-keywords').split /\s*,\s*/
    
    # hide all projects
    $('.gallery').fadeOut {
      complete: ->
        
        # replace gallery with the original one
        $(this).html $.projects.html()

        # filter
        $(this).find('li').each ->
          classes = $(this).attr('class').split ' '
          intersection = array_intersection keywords, classes
          $(this).remove() if intersection.length == 0
  
        # show all projects
        $(this).fadeIn()
    }

array_intersection = (a, b) ->
  $.grep a, (i) ->
    $.inArray(i, b) > -1
