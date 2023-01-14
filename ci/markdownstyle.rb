# frozen_string_literal: true

# Start with all built-in rules.
# https://github.com/markdownlint/markdownlint/blob/master/docs/RULES.md
all

# Override default parameters for some built-in rules.
# https://github.com/markdownlint/markdownlint/blob/master/docs/creating_styles.md#parameters

# Ignore line length in code blocks.
rule 'MD013', line_length: 120, ignore_code_blocks: true

# Ordered lists should use :ordered
rule 'MD029', style: 'ordered'

# First line should be a top-level header
exclude_rule 'MD041'

# Emphasis used instead of header
exclude_rule 'MD036'
