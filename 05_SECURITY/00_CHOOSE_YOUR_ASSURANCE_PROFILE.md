# Security and assurance profiles

Choose the profile that matches the **consequences of failure**, not the size of the codebase.

| Profile | Typical use | Real users/data? | Release rigor |
|---|---|---:|---|
| STARTER | learning, local prototype | preferably no | basic |
| PRODUCTION | public/internal real service | yes | strong |
| HIGH ASSURANCE | high-impact or regulated systems | often | very strong + independent review |

The profile files define a minimum control set:
- `PROFILES/01_STARTER_PROFILE.md`
- `PROFILES/02_PRODUCTION_PROFILE.md`
- `PROFILES/03_HIGH_ASSURANCE_PROFILE.md`

If you are unsure, choose the higher profile until the risk is understood.
