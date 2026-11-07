import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import unittest
from pathlib import Path

# Add tests/unit to path
sys.path.insert(0, str(Path('tests/unit').resolve()))
import test_rules_engine
import test_lifecycle_fsm
import test_risk_engine
import test_data_consistency
import test_priority_engine
import test_auth_rbac
import test_guidebook_compliance

passed = 0
failed = 0

tests = [
    test_rules_engine.test_beneficiary_rule_passes_with_aicte,
    test_rules_engine.test_beneficiary_rule_fails_without_aicte,
    test_rules_engine.test_tenure_rule_validates_minimum_60_months,
    test_rules_engine.test_amount_rule_validates_15_lakh_slab,
    test_lifecycle_fsm.test_valid_sequential_transitions,
    test_lifecycle_fsm.test_illegal_arbitrary_transition_blocked,
    test_risk_engine.test_clean_fdr_scores_low,
    test_risk_engine.test_mismatch_and_tamper_scores_critical,
    test_risk_engine.test_extreme_risk_triggers,
    test_data_consistency.test_canonical_institution_names,
    test_data_consistency.test_no_institution_has_two_names,
    test_priority_engine.test_priority_ranking_order,
    test_auth_rbac.test_safe_redirect,
    test_auth_rbac.test_rate_limit_lockout,
    test_auth_rbac.test_rbac_and_tenant_boundary,
    test_guidebook_compliance.test_tenant_boundary_isolation,
    test_guidebook_compliance.test_case_officer_cannot_issue_final_approval,
    test_guidebook_compliance.test_system_admin_blocked_from_altering_case_decisions,
    test_guidebook_compliance.test_optimistic_concurrency_conflict,
    test_guidebook_compliance.test_source_unavailable_is_not_fraud,
    test_guidebook_compliance.test_digital_twin_claims_never_overwrite_canonical_facts
]

print('=== RUNNING UNIT TEST SUITE ===')
for t in tests:
    try:
        t()
        print(f'✓ {t.__name__} PASSED')
        passed += 1
    except Exception as e:
        print(f'✗ {t.__name__} FAILED: {e}')
        failed += 1

print(f'\nResults: {passed} passed, {failed} failed.')
if failed > 0:
    sys.exit(1)
