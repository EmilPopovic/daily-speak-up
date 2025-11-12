from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe import emailpassword, session
from ..api.config import get_settings


def init_supertokens():
    """Initialize SuperTokens with configuration"""
    settings = get_settings()
    
    init(
        app_info=InputAppInfo(
            app_name=settings.app_name,
            api_domain=settings.api_domain,
            website_domain=settings.website_domain,
            api_base_path=settings.api_base_path,
            website_base_path="/auth"
        ),
        supertokens_config=SupertokensConfig(
            connection_uri=settings.supertokens_connection_uri,
            api_key=settings.supertokens_api_key,
        ),
        framework='fastapi',
        recipe_list=[
            emailpassword.init(),
            session.init(
                cookie_same_site="lax",
                cookie_secure=settings.environment == "production",
            )
        ]
    )
