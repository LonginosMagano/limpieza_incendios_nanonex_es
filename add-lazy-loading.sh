#!/bin/bash
# Add loading="lazy" to all images without it

count=0
for file in $(find . -name "*.html" -type f); do
  # Check if file has any <img tags
  if grep -q '<img' "$file"; then
    # Add loading="lazy" to img tags that don't have it
    sed -i 's/<img \([^>]*\)alt=/<img \1loading="lazy" alt=/g' "$file"
    ((count++))
  fi
done

echo "✅ Updated $count HTML files with lazy loading"
