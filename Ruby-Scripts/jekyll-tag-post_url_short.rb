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

# _plugins/post_url_short_tag.rb
module Jekyll
  class PostUrlShortTag < Liquid::Tag
    def initialize(tag_name, input, tokens)
      super
      @input = input.strip
    end

    def render(context)
      puts "Executing tag 'post_url_short', input: '#{@input}'"
      # Splitting the text inputted when the tag was called (argument)
      date = @input[0...10]  # Extract the first 10 characters as date
      puts "\tDate extracted from input: '#{date}'"          
      slug = @input[11..-1]  # Extract from the 12th character to the end as slug
      puts "\tSlug extracted from input: '#{slug}'"          
      
      # We are considering slug as the text after the date in the filename of the post file.
      # If we were specifically checking the slug we would go `p.data['slug']`, but it's
      # not the case - we consider the slug the last part of the file name (in `YYYY-MM-DD-example.md`  
      # it would be `example`, ignoring the front matter). This assumes that filenames are unique.
      site = context.registers[:site]
      post = site.posts.docs.find { |p| p.date.strftime('%Y-%m-%d') == date && p.basename.split('.').first[11..-1] == slug }
      if post
        puts "\tPost found with title '#{post.data['title']}', of date '#{post.data['date']}'"
      else
        puts "\tPOST NOT FOUND"
      end
      post.url if post
    end
  end
end

Liquid::Template.register_tag('post_url_short', Jekyll::PostUrlShortTag)
