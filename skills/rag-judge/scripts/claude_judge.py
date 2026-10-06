"""Build a Ragas judge backed by Claude.

    from claude_judge import claude_judge
    llm = claude_judge("claude-haiku-4-5-20251001")
    result = await metric.ascore(llm=llm, response=text)

Use this instead of calling Ragas's llm_factory directly. It fixes two things:
Ragas always sends temperature and top_p, which the current Anthropic SDK rejects,
and newer Claude models can reply with a thinking block that Ragas can't parse.

Reads ANTHROPIC_API_KEY from the environment. Never prints it.
"""
import os
import sys
import warnings

warnings.filterwarnings("ignore")

import anthropic
from ragas.llms import llm_factory

DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def claude_judge(model=DEFAULT_MODEL, max_tokens=1024):
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("Set ANTHROPIC_API_KEY first.")
    client = anthropic.AsyncAnthropic()
    llm = llm_factory(model, provider="anthropic", client=client, max_tokens=max_tokens)
    llm.model_args.pop("temperature", None)
    llm.model_args.pop("top_p", None)
    # A pass or fail verdict needs no thinking, and a thinking block breaks Ragas's parser.
    # Haiku 4.5 turns it off with "disabled"; Sonnet 5.5 rejects that and takes
    # "between_tools". Those two are the tested judge models. Other models get no thinking
    # setting at all; if their replies fail to parse, use one of the two.
    if model.startswith("claude-haiku-4"):
        llm.model_args["thinking"] = {"type": "disabled"}
    elif model.startswith("claude-sonnet-5-5"):
        llm.model_args["thinking"] = {"type": "between_tools"}
    return llm
