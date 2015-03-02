$ ->

  # save the initial status of the gallery
  $.projects = $('.gallery').clone()

  # enable filter
  $('.filter').find('li').click ->

    # toggle class
    $(this).parent().find('li').removeClass 'active'
    $(this).addClass 'active'

    # get keywords
    target = $(this).attr('data-keywords').replace ' ', ''
    keywords = if target.indexOf(',') then target.split(',') else [target]
    
    # hide all projects
    projects = $('.gallery')
    projects.fadeOut {
      complete: ->
        
        # replace gallery with the original one
        $(this).html $.projects.html()

        # filter
        projects.find('li').each ->
          classes = $(this).attr('class').split ' '
          intersection = array_intersection keywords, classes
          $(this).remove() if intersection.length == 0
  
        # show all projects
        projects.fadeIn()
    }

array_intersection = (a, b) ->
  $.grep a, (i) ->
    $.inArray(i, b) > -1
