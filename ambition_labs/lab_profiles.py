from edc_lab import LabProfile

from .panels import (
    wb_panel, csf_pkpd_panel, qpcr_csf_panel, csf_panel,
    csf_stop_panel, csf_chemistry_panel, qpcr23_blood_panel,
    cd4_panel, viral_load_panel, fbc_panel, chemistry_panel,
    chemistry_alt_panel, serum_panel, plasma_buffycoat_panel,
    qpcr_blood_panel, pk_plasma_panel_t2, pk_plasma_panel_t4,
    pk_plasma_panel_t7, pk_plasma_panel_t12, pk_plasma_panel_t23)

lab_profile = LabProfile(
    name='ambition_lab_profile',
    requisition_model='ambition_subject.subjectrequisition')


lab_profile.add_panel(wb_panel)
lab_profile.add_panel(csf_pkpd_panel)
lab_profile.add_panel(qpcr_csf_panel)
lab_profile.add_panel(csf_panel)
lab_profile.add_panel(csf_stop_panel)
lab_profile.add_panel(csf_chemistry_panel)  # goes to PMH
lab_profile.add_panel(cd4_panel)
lab_profile.add_panel(viral_load_panel)
lab_profile.add_panel(fbc_panel)
lab_profile.add_panel(chemistry_panel)
lab_profile.add_panel(chemistry_alt_panel)
lab_profile.add_panel(serum_panel)
lab_profile.add_panel(plasma_buffycoat_panel)
lab_profile.add_panel(qpcr_blood_panel)
lab_profile.add_panel(qpcr23_blood_panel)
lab_profile.add_panel(pk_plasma_panel_t2)  # TODO: For Blantyre only
lab_profile.add_panel(pk_plasma_panel_t4)
lab_profile.add_panel(pk_plasma_panel_t7)
lab_profile.add_panel(pk_plasma_panel_t12)
lab_profile.add_panel(pk_plasma_panel_t23)
