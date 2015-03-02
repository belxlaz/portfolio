$ ->

  # PNG fallback for SVG images
  if !Modernizr.svg
    $('img[src*="svg"]').attr 'src', ->
      $(this).attr('src').replace '.svg', '.png'
