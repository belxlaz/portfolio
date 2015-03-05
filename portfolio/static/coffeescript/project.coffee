$ ->

  # image tag to parent background
  $('#project-content').find('.content').find('.wide').find('img').each ->
    source =$(this).attr 'src'
    background = 'url(' + source + ')'
    $(this).parent().css 'background-image', background
