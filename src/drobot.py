# -*- coding: utf-8 -*-
from src import functionality

from discord.ext import commands

from typing import Tuple, Dict


class DROBot():
    def __init__(self, production: bool = True):
        guild_details, token = self._setup(production)
        bot = commands.Bot(command_prefix="$")
        functionality.Functionality(bot=bot, guild_details=guild_details)
        bot.run(token)

    @staticmethod
    def _setup(production: bool) -> Tuple[Dict, str]:
        # Production should be True for use in public servers, False for test server
        if production:
            token_file = 'src/guild_specific/dro.token'
            from src.guild_specific.dro import DRO_discord
            guild_details = DRO_discord()
        else:
            token_file = 'src/guild_specific/test.token'
            from src.guild_specific.test import Test_discord
            guild_details = Test_discord()
            print('THIS IS A TEST BOT')

        try:
            with open(token_file, 'r') as f:
                token = f.read()
            if not token:
                raise RuntimeError
        except (OSError, RuntimeError):
            raise RuntimeError(f'No token file or contents found: {token_file}')

        return guild_details, token
