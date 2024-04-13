# A Jekyll hook that prints a summary of the site's content at build (after rendering).
#
# The summary includes the following information:
#   - Total number of posts in the site.
#   - List of categories with the number of posts in each category.
#   - List of tags with the number of posts associated with each tag.
#
# Example:
#   ```
#   --------------------
#   --- Site Summary ---
#   --------------------
#
#   Total number of posts: 10
#
#   List of categories with post counts:
#     5   category1
#     3   category2
#     2   category3
#
#   List of tags with post counts:
#     7   tag1
#     5   tag2
#     3   tag3
#
#   --------------------
#   -- End of Summary --
#   --------------------
#   ```
#
# More at: https://aloneinthesea.com/2024/04/site-summary


module Jekyll
    class SiteSummaryHook
      Jekyll::Hooks.register :site, :post_render do |site|
        puts "\n--------------------"
        puts "--- Site Summary ---"
        puts "--------------------\n\n"
  
        # Total number of posts
        total_posts = site.posts.docs.size
        puts "Total number of posts: #{total_posts}\n\n"
  
        # List of categories and number of posts in each
        categories = Hash.new(0)
        site.posts.docs.each do |post|
          (post.data['categories'] || []).each { |category| categories[category] += 1 }
        end
  
        puts "List of categories with post counts:"
        categories.sort_by { |category, count| -count }.each do |category, count|
          puts "\t#{count}\t#{category}"
        end
  
        # Example: List of tags
        tags = Hash.new(0)
        site.posts.docs.each do |post|
          (post.data['tags'] || []).each { |tag| tags[tag] += 1 }
        end
        puts "\nList of tags with post counts:"        
        tags.sort_by { |tag, count| -count }.each do |tag, count|
          puts "\t#{count}\t#{tag}"          
        end
        puts "\n--------------------"
        puts "-- End of Summary --"
        puts "--------------------\n\n"        
      end
    end
  end