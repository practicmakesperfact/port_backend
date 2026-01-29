from django.core.management.base import BaseCommand
from profiles.models import Profile
from skills.models import SkillCategory, Skill
from projects.models import Project

class Command(BaseCommand):
    help = 'Setup default portfolio data'

    def handle(self, *args, **options):
        # Create default profile
        profile, created = Profile.objects.get_or_create(
            defaults={
                'name': 'Haymanot Asmare',
                'title': 'Full Stack Software Engineer',
                'bio': "I'm a passionate Full Stack Software Engineer with extensive experience in building scalable web applications and creating exceptional digital experiences. My expertise spans across modern frontend frameworks, robust backend systems, and intuitive UI/UX design.",
                'detailed_bio': "I specialize in transforming complex business requirements into elegant, efficient solutions that drive measurable results. With a strong foundation in both engineering and design principles, I bridge the gap between technical implementation and user experience.",
                'years_experience': 5,
                'projects_delivered': 50,
                'happy_clients': 30,
                'github_url': 'https://github.com',
                'linkedin_url': 'https://linkedin.com',
                'upwork_url': 'https://upwork.com',
                'twitter_url': 'https://twitter.com',
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Default profile created'))
        else:
            self.stdout.write(self.style.WARNING('Profile already exists'))

        # Create skill categories
        categories_data = [
            {'name': 'Frontend Development', 'icon': 'fas fa-laptop-code', 'order': 1},
            {'name': 'Backend Development', 'icon': 'fas fa-server', 'order': 2},
            {'name': 'Databases', 'icon': 'fas fa-database', 'order': 3},
            {'name': 'Mobile Development', 'icon': 'fas fa-mobile-alt', 'order': 4},
            {'name': 'Tools & Collaboration', 'icon': 'fas fa-tools', 'order': 5},
            {'name': 'Soft Skills', 'icon': 'fas fa-users', 'order': 6},
        ]

        for cat_data in categories_data:
            category, created = SkillCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'icon': cat_data['icon'], 'order': cat_data['order']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))

        # Create skills
        skills_data = [
            # Frontend
            {'name': 'React', 'category': 'Frontend Development', 'icon': 'fab fa-react'},
            {'name': 'JavaScript', 'category': 'Frontend Development', 'icon': 'fab fa-js'},
            {'name': 'Tailwind CSS', 'category': 'Frontend Development', 'icon': 'fab fa-css3-alt'},
            {'name': 'Bootstrap', 'category': 'Frontend Development', 'icon': 'fab fa-bootstrap'},
            
            # Backend
            {'name': 'Django', 'category': 'Backend Development', 'icon': 'fab fa-python'},
            {'name': 'Django REST Framework', 'category': 'Backend Development', 'icon': 'fab fa-python'},
            {'name': 'FastAPI', 'category': 'Backend Development', 'icon': 'fab fa-python'},
            
            # Databases
            {'name': 'PostgreSQL', 'category': 'Databases', 'icon': 'fas fa-database'},
            {'name': 'MySQL', 'category': 'Databases', 'icon': 'fas fa-database'},
            {'name': 'SQLite', 'category': 'Databases', 'icon': 'fas fa-database'},
            {'name': 'MongoDB', 'category': 'Databases', 'icon': 'fas fa-leaf'},
            
            # Mobile
            {'name': 'Flutter', 'category': 'Mobile Development', 'icon': 'fas fa-mobile'},
            
            # Tools
            {'name': 'Git', 'category': 'Tools & Collaboration', 'icon': 'fab fa-git-alt'},
            {'name': 'GitHub', 'category': 'Tools & Collaboration', 'icon': 'fab fa-github'},
            
            # Soft Skills
            {'name': 'Communication', 'category': 'Soft Skills', 'icon': 'fas fa-comments'},
            {'name': 'Teamwork', 'category': 'Soft Skills', 'icon': 'fas fa-users'},
            {'name': 'Problem Solving', 'category': 'Soft Skills', 'icon': 'fas fa-lightbulb'},
        ]

        for skill_data in skills_data:
            category = SkillCategory.objects.get(name=skill_data['category'])
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                category=category,
                defaults={'icon': skill_data['icon']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created skill: {skill.name}'))

        # Create projects
        projects_data = [
            {
                'title': 'CFITP – Client Feedback and Issue Tracking Portal',
                'description': 'A secure and scalable enterprise web application designed to manage client feedback, track issues, and improve communication efficiency for AITB.',
                'icon': 'fas fa-chart-line',
                'tech_stack': 'React, Tailwind CSS, Django, DRF, PostgreSQL',
                'features': 'Role-based authentication, Feedback submission & tracking, Real-time issue tracking, Admin dashboard & analytics',
                'order': 1
            },
            {
                'title': 'Yoni Central Electronics – Online Shopping Platform',
                'description': 'A full-featured e-commerce web application developed for an electronics retail business, enabling online product browsing, purchasing, and order management.',
                'icon': 'fas fa-shopping-cart',
                'tech_stack': 'JavaScript, Bootstrap, Django, SQLite3',
                'features': 'Product catalog & categories, Shopping cart functionality, Order management system, Admin product control',
                'order': 2
            },
            {
                'title': 'BIIB Designs – Architectural Company Website',
                'description': 'A modern and visually appealing corporate website developed for an architectural and design company to showcase services, portfolios, and company identity.',
                'icon': 'fas fa-building',
                'tech_stack': 'React, Tailwind CSS, Django, DRF',
                'features': 'Portfolio gallery, Service presentation, Contact & inquiry forms, Responsive design',
                'order': 3
            }
        ]

        for proj_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=proj_data['title'],
                defaults={
                    'description': proj_data['description'],
                    'icon': proj_data['icon'],
                    'tech_stack': proj_data['tech_stack'],
                    'features': proj_data['features'],
                    'order': proj_data['order']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {project.title}'))

        self.stdout.write(self.style.SUCCESS('Default data setup completed!'))
