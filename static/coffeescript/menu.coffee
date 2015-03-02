$ ->

  # scroll to hash on load
  animate_scroll_to location.hash if location.hash

  # build burger menu
  burger_tag = document.createElement('div')
  burger_tag.setAttribute 'id', 'burger'
  for num in [1..3]
    bar = document.createElement('div')
    bar.setAttribute 'class', 'bar'
    burger_tag.appendChild bar

  # append burger and add `loaded` classes
  $('#menu').addClass('loaded').append burger_tag
  $('.menu-mobile').addClass 'loaded' 

  # mobile menu toggle
  $('#burger').click toggle_menu

  # menu navigation
  $('.menu-links').find('a').click menu_click
  $('#top').find('a').click menu_click

menu_click = ->

  console.log 'hey'
  # check if is an anchor within the same page
  same_url = location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
  same_host = location.hostname == this.hostname
  if same_url and same_host
    
    # scroll, hide the menu (mobile only), and prevent click action
    href = $(this).attr 'href'
    hash = href.substr href.indexOf('#')
    toggle_menu() if $('#menu').hasClass 'active'
    animate_scroll_to hash
    return false

toggle_menu = ->
  burger = $('#burger')
  if burger

    # toggle classes
    menu = burger.parent()
    toggle_menu_classes menu
    toggle_menu_classes $('.menu-mobile')

    # enable/disable scroll
    if menu.hasClass 'active'
      $(window).bind 'touchmove', (e) -> e.preventDefault()
    else
      $(window).unbind 'touchmove'

toggle_menu_classes = (obj) ->
  if obj.hasClass('loaded')
    obj.removeClass 'loaded'
    obj.addClass 'inactive'
  obj.toggleClass 'active'
  obj.toggleClass 'inactive'

animate_scroll_to = (target) ->
  obj = $(target)
  if obj
    $('html, body').animate { scrollTop: obj.offset().top }, 333
