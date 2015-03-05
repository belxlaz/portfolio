$ ->
  obj = $('footer').find('li').first().removeClass 'js'
  setTimeout(ofuscated, 10000)

ofuscated = ->
  obj = $('footer').find('li').first().find('a')
  original = obj.attr('href')
  fix1 = original.replace ' at ', '@'
  fix2 = fix1.replace ' dot ', '.'
  obj.attr 'href', dot
