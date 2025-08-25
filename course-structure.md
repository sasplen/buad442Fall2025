# Course Folder Structure - Challenge-Focused Organization

## Recommended Organization

```
buad442Fall2025/
├── README.md                           # Course overview and getting started
├── course-structure.md                 # This file - folder organization guide
├── syllabus/                           # Course syllabus and policies
│   ├── syllabus.md
│   ├── grading-rubric.md
│   └── academic-integrity.md
├── challenges/                         # All challenges organized by topic
│   ├── 01-data-quality-challenge/
│   │   ├── README.md                   # Challenge overview and objectives
│   │   ├── instructions.md             # Detailed step-by-step instructions
│   │   ├── slides/                     # Topic slides
│   │   ├── starter-code/               # Starter code and templates
│   │   │   ├── r/
│   │   │   ├── python/
│   │   │   ├── quarto/
│   │   │   └── dot/
│   │   ├── datasets/                   # Challenge-specific datasets
│   │   ├── expected-outputs/           # Example outputs for reference
│   │   ├── grading-criteria.md         # Specific grading criteria
│   │   ├── solutions/                  # Instructor solutions (private)
│   │   └── student-submissions/        # Individual student folders
│   │       ├── student001/
│   │       ├── student002/
│   │       ├── student003/
│   │       └── ...
│   ├── 02-visualization-challenge/
│   │   ├── README.md
│   │   ├── instructions.md
│   │   ├── slides/
│   │   ├── starter-code/
│   │   ├── datasets/
│   │   ├── expected-outputs/
│   │   ├── grading-criteria.md
│   │   ├── solutions/
│   │   └── student-submissions/
│   │       ├── student001/
│   │       ├── student002/
│   │       └── ...
│   ├── 03-statistical-models-challenge/
│   ├── 04-machine-learning-challenge/
│   ├── 05-interpretability-challenge/
│   ├── 06-communication-challenge/
│   ├── 07-decision-trees-challenge/
│   └── 08-final-project/
│       ├── README.md
│       ├── project-guidelines.md
│       ├── slides/
│       ├── datasets/
│       ├── grading-criteria.md
│       └── student-submissions/
│           ├── student001/
│           ├── student002/
│           └── ...
├── student-portfolios/                 # Individual student main folders
│   ├── student001/
│   │   ├── README.md                   # Student introduction and portfolio
│   │   ├── profile.md                  # Student profile and goals
│   │   ├── reflections/                # Weekly reflections and learning notes
│   │   │   ├── week01-reflection.md
│   │   │   ├── week02-reflection.md
│   │   │   └── ...
│   │   ├── progress-tracker.md         # Self-assessment and progress tracking
│   │   └── final-portfolio.md          # Final portfolio summary
│   ├── student002/
│   └── ...
├── resources/                          # General course resources
│   ├── tool-setup-guides/
│   │   ├── github-setup.md
│   │   ├── cursor-ai-setup.md
│   │   ├── quarto-setup.md
│   │   ├── r-setup.md
│   │   ├── python-setup.md
│   │   └── dot-setup.md
│   ├── templates/                      # Reusable templates
│   │   ├── challenge-submission-template/
│   │   ├── report-template/
│   │   ├── reflection-template.md
│   │   └── presentation-template/
│   ├── best-practices/
│   │   ├── git-best-practices.md
│   │   ├── coding-standards.md
│   │   └── documentation-standards.md
│   ├── common-mistakes/
│   │   ├── data-quality-mistakes.md
│   │   ├── visualization-mistakes.md
│   │   └── interpretation-mistakes.md
│   └── reference-materials/
│       ├── cheat-sheets/
│       ├── tutorials/
│       └── additional-reading/
├── grading/                            # Grading materials (private)
│   ├── rubrics/
│   ├── grade-tracking/
│   └── feedback-templates/
└── admin/                              # Administrative files
    ├── course-schedule.md
    ├── contact-info.md
    ├── announcements.md
    └── student-list.md
```

## Challenge Structure Details

Each challenge folder contains:

```
challenge-name/
├── README.md                           # Challenge overview, objectives, and learning outcomes
├── instructions.md                     # Detailed step-by-step instructions
├── slides/                             # Topic presentation slides
│   ├── slides.qmd                      # Quarto presentation
│   ├── slides.html                     # Rendered HTML
│   └── slides.pdf                      # PDF version
├── starter-code/                       # Starter code and templates
│   ├── r/
│   │   ├── main.R
│   │   ├── functions.R
│   │   └── template.qmd
│   ├── python/
│   │   ├── main.py
│   │   ├── functions.py
│   │   └── template.qmd
│   ├── quarto/
│   │   ├── report.qmd
│   │   └── presentation.qmd
│   └── dot/
│       ├── decision-tree.dot
│       └── flowchart.dot
├── datasets/                           # Challenge-specific datasets
│   ├── raw-data/
│   ├── processed-data/
│   └── data-dictionary.md
├── expected-outputs/                   # Example outputs for reference
│   ├── sample-reports/
│   ├── sample-visualizations/
│   └── sample-analyses/
├── grading-criteria.md                 # Specific grading criteria and rubrics
├── solutions/                          # Instructor solutions (private)
│   ├── r-solution/
│   ├── python-solution/
│   └── sample-outputs/
└── student-submissions/                # Individual student folders
    ├── student001/
    │   ├── submission.md               # Student's submission summary
    │   ├── code/                       # Student's code files
    │   ├── outputs/                    # Student's generated outputs
    │   ├── report.qmd                  # Student's Quarto report
    │   └── reflection.md               # Student's reflection on the challenge
    ├── student002/
    └── ...
```

## Student Portfolio Structure

Each student's main portfolio folder:

```
student-portfolios/student001/
├── README.md                           # Student introduction and portfolio overview
├── profile.md                          # Student profile, goals, and background
├── reflections/                        # Weekly reflections and learning notes
│   ├── week01-reflection.md
│   ├── week02-reflection.md
│   ├── week03-reflection.md
│   ├── week04-reflection.md
│   ├── week05-reflection.md
│   ├── week06-reflection.md
│   ├── week07-reflection.md
│   └── week08-reflection.md
├── progress-tracker.md                 # Self-assessment and progress tracking
├── final-portfolio.md                  # Final portfolio summary
└── .gitignore                          # Appropriate gitignore for their tools
```

## Key Benefits of This Structure

1. **Challenge-Focused**: Easy to find all materials related to a specific challenge
2. **Student Organization**: Clear separation of student work by individual
3. **Scalability**: Easy to add new challenges or students
4. **Grading Efficiency**: All student submissions for a challenge in one place
5. **Resource Management**: Centralized resources and templates
6. **Version Control**: Git-friendly structure for tracking changes
7. **Portfolio Building**: Students can build comprehensive portfolios
8. **Instructor Workflow**: Streamlined grading and feedback process

## Workflow Benefits

- **For Students**: Clear submission locations and portfolio building
- **For Instructors**: Easy grading by challenge and tracking individual progress
- **For Course Management**: Scalable structure for multiple sections and semesters
