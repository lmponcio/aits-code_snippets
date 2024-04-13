# A Jekyll hook that automatically assigns categories to posts based on their directory names
#
# The hook does the following:
#   - Determines the directory name where the post file resides.
#   - If the directory is not the default "_posts" and the post does not already have categories assigned,
#     it assigns the directory name as a category to the post (atm, it only works with the `categories` key).      
#   - Log messages are printed indicating what category has been assigned to which post.
#
# Example:
#   - A post located in "_posts/tech/sample-post.md" will get 'tech' as its category if it has no categories set.
#   - If you move that post to "_posts/news/sample-post.md", its category now will be 'news'.
#
# More at: 
#   - https://aloneinthesea.com/2024/04/ruby-hook-jekyll
#   - https://aloneinthesea.com/2024/04/jekyll-front-matter-update-with-python


Jekyll::Hooks.register :posts, :pre_render do |post, payload|
    # Extract the category from the post's directory
    dirname = File.basename(File.dirname(post.path))
  
    # Assign the category to the post's front matter
    if dirname != "_posts" && (post.data['categories'].nil? || post.data['categories'].empty?)
        post.data['categories'] = [dirname]
        puts "Categories assigned to post #{post.data['title']}: #{dirname}"
    end
end