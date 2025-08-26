# BUAD 442 Course Introduction - Quarto Presentation

This folder contains a comprehensive Quarto presentation slide deck for the BUAD 442 course introduction.

## Files

- `course-introduction.qmd` - The main Quarto presentation file
- `README.md` - This documentation file

## Features

### Presentation Features
- **PowerPoint Format** - Standard PPTX presentation format
- **Professional Layout** - Clean, business-appropriate design
- **Speaker Notes** - Hidden notes for presenter guidance
- **Easy Editing** - Standard PowerPoint compatibility
- **Wide Compatibility** - Works with PowerPoint, Google Slides, and other presentation software

### Content Structure
1. **Welcome Slide** - Course introduction and instructor info
2. **Course Overview** - What students will learn
3. **Course Objectives** - Specific learning outcomes
4. **Course Structure** - Weekly format and components
5. **Technology Stack** - Tools and software used
6. **Prerequisites** - Required background knowledge
7. **Assessment Breakdown** - Grading structure
8. **Course Schedule** - Semester roadmap
9. **Student Portfolios** - Portfolio concept explanation
10. **Course Policies** - Important guidelines
11. **Getting Started** - Next steps for students
12. **Resources & Support** - Help and support options
13. **Questions & Discussion** - Interactive session
14. **Thank You** - Closing slide with contact info

## How to Use

### Prerequisites
1. Install [Quarto](https://quarto.org/docs/get-started/)
2. Install [R](https://www.r-project.org/) (optional, for R code execution)
3. Install [Python](https://www.python.org/) (optional, for Python code execution)

### Rendering the Presentation
```bash
# Navigate to the CourseIntroduction folder
cd topics/CourseIntroduction

# Render the presentation
quarto render course-introduction.qmd

# Render with live preview (recommended for editing)
quarto preview course-introduction.qmd
```

### Output Formats
The presentation renders to:
- **PowerPoint** - PPTX format (default)
- **HTML** - Web presentation (requires additional setup)
- **PDF** - Static PDF version (requires additional setup)

## Customization

### Personal Information
Update the following placeholders in `course-introduction.qmd`:
- `[Your Name]` - Your name as instructor
- `[Schedule]` - Your office hours
- `[your.email@university.edu]` - Your email address
- `[Building/Room]` - Your office location
- `[Date]` and `[Topic]` - Next class information

### Content Modifications
1. **Edit Slides** - Modify content in the `.qmd` file
2. **Add/Remove Slides** - Use `---` to separate slides
3. **Speaker Notes** - Add notes in `::: {.notes}` blocks
4. **Styling** - Use PowerPoint's built-in themes and formatting options

### Adding New Slides
```markdown
---

## New Slide Title {.center}

### Subtitle

Content goes here...

::: {.notes}
Speaker notes for this slide.
:::
```

### PowerPoint Formatting
The presentation uses standard PowerPoint formatting:
- **Bold text** - For emphasis and key points
- **Bullet points** - For lists and structured content
- **Tables** - For organized data presentation
- **Speaker notes** - For presenter guidance (hidden in final presentation)

## Tips for Presenting

### Before Presentation
1. **Test Rendering** - Ensure all slides render correctly
2. **Check Notes** - Review speaker notes for each slide
3. **Practice Navigation** - Familiarize yourself with controls
4. **Test Equipment** - Verify projector and audio setup

### During Presentation
1. **Use Speaker Notes** - View notes in PowerPoint's presenter view
2. **Navigation** - Use arrow keys, mouse, or remote
3. **Fullscreen** - Use PowerPoint's fullscreen presentation mode
4. **Notes View** - Access speaker notes during presentation

### PowerPoint Shortcuts
- **F5** - Start presentation from beginning
- **Shift+F5** - Start presentation from current slide
- **Space/Right Arrow** - Next slide
- **Left Arrow** - Previous slide
- **B** - Black screen
- **W** - White screen
- **ESC** - End presentation

## Troubleshooting

### Common Issues
1. **PowerPoint Compatibility** - Ensure PowerPoint version supports the file format
2. **Images Not Displaying** - Check file paths and permissions
3. **Font Issues** - Use standard fonts for maximum compatibility
4. **Layout Problems** - Check slide layouts in PowerPoint

### Getting Help
- [Quarto Documentation](https://quarto.org/docs/)
- [PowerPoint Support](https://support.microsoft.com/en-us/powerpoint)
- [Quarto Community](https://github.com/quarto-dev/quarto/discussions)

## File Structure
```
topics/CourseIntroduction/
├── course-introduction.qmd    # Main presentation file
├── README.md                  # This documentation
└── _quarto.yml               # Quarto configuration (auto-generated)
```

## Version History
- **v1.0** - Initial creation with comprehensive course introduction slides
- Includes speaker notes and PowerPoint-compatible formatting
