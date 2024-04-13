# This module defines a custom Liquid tag for Jekyll to generate URLs for posts using a shortened matching method ("date-slug" instead of "path-date-slug").
# (as a condition, in your site you shouldn't have two posts on the same date with the same slug)
# 
# Usage:
#   - In your Liquid templates, use `{% post_url_short YYYY-MM-DD-slug %}` to generate a URL for a post.
#
# Example:
#   To identify "_posts/tech/sample-post.md", you will just use `{% post_url_short 2023-04-12-example-post %}`,
#   and if you move sample post to "_posts/news/sample-post.md", there is no need to change the reference.
#
# More at:
#   - https://aloneinthesea.com/2024/04/ruby-jekyll-custom-tag
#   - https://stackoverflow.com/questions/53323570/jekyll-internal-post-links/78280198#answer-78280198

module Jekyll
  class PostUrlShortTag < Liquid::Tag
    def initialize(tag_name, input, tokens)
      super
      @input = input.strip
    end

    def render(context)
      site = context.registers[:site]
      date, slug = @input.split('-')
      post = site.posts.docs.find { |p| p.date.strftime('%Y-%m-%d') == date && p.data['slug'] == slug }
      post.url if post
    end
  end
end

Liquid::Template.register_tag('post_url_short', Jekyll::PostUrlShortTag)
