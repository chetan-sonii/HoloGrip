from flask import Blueprint, render_template

from app.utils.project_data import FEATURES, IMPLEMENTATION_STEPS, PROJECT, TEAM, TECHNOLOGIES

main_bp = Blueprint("main", __name__)


def _render(template, active_page):
    return render_template(
        template,
        active_page=active_page,
        project=PROJECT,
        features=FEATURES,
        technologies=TECHNOLOGIES,
        implementation_steps=IMPLEMENTATION_STEPS,
        team=TEAM,
    )


@main_bp.get("/")
def index():
    return _render("index.html", "home")


@main_bp.get("/project")
def project():
    return _render("project.html", "project")


@main_bp.get("/implementation")
def implementation():
    return _render("implementation.html", "implementation")


@main_bp.get("/demo")
def demo():
    return _render("demo.html", "demo")


@main_bp.get("/team")
def team():
    return _render("team.html", "team")
