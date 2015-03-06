$ ->

  $('#footer li.email').removeClass 'js'
  setTimeout(ofuscated, 10000)

ofuscated = ->
  obj = $('#footer li.email a')
  original = obj.attr('href')
  fix1 = original.replace ' at ', '@'
  fix2 = fix1.replace ' dot ', '.'
  obj.attr 'href', fix2
  console.log fix2
