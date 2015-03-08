$ ->

  $.email = $('#footer li.email')
  $.email.removeClass 'js'
  setTimeout(ofuscated, 10000)

ofuscated = ->
  link = $.email.find('a')
  original = link.attr 'href'
  link.attr 'href', original.replace(' at ', '@').replace(' dot ', '.')
