"""Multi-discrete head of MADRLCitytleranflexresdr (SPEC-015 D-M3-9): ``args.action_branches = (K, L)``.

K branches (one per equipment) of L levels each, n_actions = K * L. Without the attribute the head is the
author's single categorical of n_actions, (1, n_actions).
"""


def action_branches(args):
    branches = getattr(args, 'action_branches', None)
    if branches:
        return int(branches[0]), int(branches[1])
    return 1, int(args.n_actions)
