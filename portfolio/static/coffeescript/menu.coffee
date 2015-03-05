$ ->

  # useful vars
  $.is_home = $('body').hasClass 'home'
  $.highlighted = false
  $.window = $(window)

  # scroll to hash on load
  animate_scroll_to location.hash if location.hash and $is_home

  # highlight menu (desktop only)
  menu_highlight()
  $.window.scroll menu_highlight

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
  $('#top').find('h1').find('a').click menu_click

menu_click = ->

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
  if burger.css('display') == 'block'

    # toggle classes
    menu = burger.parent()
    toggle_menu_classes menu
    toggle_menu_classes $('.menu-mobile')

    # enable/disable scroll
    if menu.hasClass 'active'
      $.window.bind 'touchmove', (e) -> e.preventDefault()
    else
      $.window.unbind 'touchmove'

toggle_menu_classes = (obj) ->
  if obj.hasClass('loaded')
    obj.removeClass 'loaded'
    obj.addClass 'inactive'
  obj.toggleClass 'active'
  obj.toggleClass 'inactive'

animate_scroll_to = (target) ->
  obj = $(target)
  if obj
    pos = obj.offset().top
    pos -= $('#about').offset().top if $.is_home
    $('html, body').animate { scrollTop: pos }, 333

scroll_map = ->

  # suport vars
  projects = $('#projects')
  contacts = $('#contacts')
  has_projects = if $.is_home and projects.length > 0 then true else false
  has_contacts = if $.is_home and contacts.length > 0 then true else false

  # get offset
  about_pos = if $.is_home then 0 else false
  projects_pos = if has_projects then projects.offset().top else false
  contacts_pos = if has_contacts then contacts.offset().top else false

  # adjust contatcs (change on bottom, not top)
  contacts_pos -= $.window.height()

  # return
  output = {
    about: about_pos,
    projects: projects_pos,
    contacts: contacts_pos
  }

menu_highlight = ->
  if $.is_home
    pos = $.window.scrollTop()
    map = scroll_map()
    if pos > map.contacts
      menu_toggle_highlight 'contacts'
    else if pos > map.projects
      menu_toggle_highlight 'projects'
    else if pos >= map.about
      menu_toggle_highlight 'about'
    else
      $('.menu').find('a').removeClass 'active'

menu_toggle_highlight = (target) ->
  if target != $.highlighted and $.is_home
    $.highlighted = target
    $('.menu').find('a').each ->
      href = $(this).attr 'href'
      if href.indexOf('#' + target) > -1
        $(this).addClass 'active'
      else
        $(this).removeClass 'active'
