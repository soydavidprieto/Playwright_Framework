# hooks/playwright_hooks.py
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Hook para agregar comportamiento post-fallo
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)
        if page:
            # Inicia y guarda tracing
            context = page.context
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            context.tracing.stop(path=f"reports/trace_{item.name}.zip")
