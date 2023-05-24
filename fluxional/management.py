import typer
from cookiecutter.main import cookiecutter  # type: ignore
from fluxional.configs import REPOSITORY_TEMPLATE
from pydantic import BaseModel
from typing import Optional


class CreateAppModel(BaseModel):
    project_name: Optional[str] = None


cli = typer.Typer()

@cli.command()
def create_app(
    project_name: Optional[str] = None,
):
    """Create a fluxional app cli. This fetches a cookiecutter template.

    Args:
        project_name (Optional[str], optional): The project name. Defaults to None.
    """
    context = CreateAppModel(
        project_name=project_name, 
    ).dict(exclude_defaults=True)

    cookiecutter(
        REPOSITORY_TEMPLATE,
        no_input=True,
        extra_context=context,
    )

@cli.command()
def _():
    ...

def run_command_line():
    cli()