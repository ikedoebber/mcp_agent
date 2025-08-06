import os
from dotenv import load_dotenv


load_dotenv()

SMITHERY_API_KEY = os.getenv("SMITHERY_API_KEY")

MCP_SERVERS_CONFIG = {
    'sequentialthinking_tools': {
        'url': f'https://server.smithery.ai/@xinzhongyouhai/mcp-sequentialthinking-tools/mcp?api_key={SMITHERY_API_KEY}&profile=puny-bobolink-bqF3WI',
        'transport': 'streamable_http',
    },
        'calculator': {
        'url': f'https://server.smithery.ai/@githejie/mcp-server-calculator/mcp?api_key={SMITHERY_API_KEY}&profile=puny-bobolink-bqF3WI',
        'transport': 'streamable_http',
    },
#    },
#    'server-name': {
#           'url': f'',
#            'transport': 'streamable_http',
#    },
}
