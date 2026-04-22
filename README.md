# Sweeppea Plugin for Agent Zero

Official [Sweeppea](https://www.sweeppea.com) integration for [Agent Zero](https://github.com/frdel/agent-zero). Connect your Sweeppea account in seconds — no technical MCP setup required.

## What is Sweeppea?

Sweeppea is a professional sweepstakes management platform for the United States and Canada. It handles legal compliance, participant management, winner drawings, and everything needed to run legally compliant promotions.

## What this plugin does

This plugin automatically configures the **Sweeppea MCP server** (`https://mcp.sweeppea.com/`) in Agent Zero so you can manage sweepstakes through natural language conversations. Just enter your API token once and you're done.

## Requirements

This plugin requires an active **Sweeppea subscription**. Running sweepstakes in the US and Canada is legally complex — each state has its own registration requirements, bonding thresholds, eligibility rules, and prize disclosure laws. Sweeppea handles all of that: compliant official rules, multi-state eligibility, auditable winner draws, and more.

Your API token isn't just authentication — it's your access to a platform built to keep promotions legally defensible.

No account yet? [Start at sweeppea.com](https://www.sweeppea.com).

## Quick Setup

1. Install the plugin from the Agent Zero plugin store
2. Open **Settings → Plugins → Sweeppea**
3. Paste your Sweeppea API token
4. Click **Save & Connect**
5. Start chatting!

You can find your API token in your [Sweeppea account settings](https://www.sweeppea.com).

## Available Tools (70+)

| Category | Tools |
|---|---|
| Account | health_check, get_profile, get_business, get_plan |
| Sweepstakes | create, update, pause, unpause, clone, delete, fetch |
| Participants | add, get, fetch, count, delete |
| Winners | draw_winners, schedule_drawing, fetch_winners, fetch_scheduled_drawings |
| Rules | create_rule, update_rule, delete_rule, fetch_rules, create_rules_wizard |
| Entry Page | get_entry_fields, get_entry_settings, update_entry_settings |
| Groups | create, update, delete, fetch |
| Notes | create, get, update, delete, fetch (AES-256-CBC encrypted) |
| Calendar | create, get, update, delete, fetch |
| Billing | fetch_billing_consumptions, fetch_billing_transactions, fetch_wallet_transactions |
| Support | create_ticket, get_ticket, update_ticket, resolve_ticket, fetch_open/closed |
| Files | upload_file, fetch_files, delete_file, send_file |
| Todos | create_todo, fetch_todos, update_todo, delete_todo |
| Utilities | fetch_timezones, fetch_states, fetch_zipcodes, fetch_areacodes, fetch_countries |
| Testing | hello_world |

## Example Conversations

> "Create a sweepstakes for a $500 Amazon gift card, open for 30 days, US residents only."

> "Add john@example.com as a participant to my Summer Giveaway."

> "Draw 3 winners from my latest sweepstakes."

> "Generate official rules for my promotion with prizes under $5,000."

> "What's my current account plan and billing balance?"

## Legal Compliance

Sweeppea ensures all promotions are legally compliant in the US:
- Every sweepstakes includes a free Alternative Method of Entry (AMOE)
- Prizes over $5,000 with FL/NY participants require registration & bonding
- Alcohol and cannabis promotions require Age Gate (21+)
- COPPA compliance — no data collection from users under 13

Ask Agent Zero to verify compliance before launching any promotion.

## Resources

- [Sweeppea Platform](https://www.sweeppea.com)
- [MCP Documentation](https://mcpdocs.sweeppea.com)
- [MCP Endpoint](https://mcp.sweeppea.com)

## License

MIT
