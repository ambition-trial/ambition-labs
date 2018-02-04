from edc_lab import RequisitionPanel

from .aliquot_types import wb, csf
from .processing_profiles import (
    whole_blood_processing, csf_pkpd_processing_profile,
    qpcr_csf_processing_profile, csf_store_processing_profile,
    csf_stop_processing_profile, csf_chem_processing_profile,
    cd4_processing, viral_load_processing, fbc_processing,
    chemistry_processing, chemistry_alt_processing, serum_processing,
    plasma_buffycoat_processing, qpcr_blood_processing, plasma_processing)

wb_panel = RequisitionPanel(
    name='wb_storage',
    verbose_name='Whole Blood Storage',
    aliquot_type=wb,
    processing_profile=whole_blood_processing)

csf_pkpd_panel = RequisitionPanel(  # TODO: Only for Blantyre
    name='csf_pk_pd',
    verbose_name='CSF PK/PD',
    aliquot_type=csf,
    processing_profile=csf_pkpd_processing_profile)

qpcr_csf_panel = RequisitionPanel(
    name='qpcr_csf',
    verbose_name='qPCR CSF',
    aliquot_type=csf,
    processing_profile=qpcr_csf_processing_profile)

csf_panel = RequisitionPanel(
    name='csf_test_and_store',
    verbose_name='CSF Test and Store',
    aliquot_type=csf,
    processing_profile=csf_store_processing_profile)

csf_stop_panel = RequisitionPanel(  # TODO: Blantyre only.
    name='csf_stop_cm',
    verbose_name='CSF STOP-CM',
    aliquot_type=csf,
    processing_profile=csf_stop_processing_profile)

csf_chemistry_panel = RequisitionPanel(
    name='csf_chem_haem_routine',
    verbose_name='CSF Chem and Haem Routine',
    aliquot_type=csf,
    processing_profile=csf_chem_processing_profile)

cd4_panel = RequisitionPanel(
    name='cd4',
    verbose_name='CD4',
    aliquot_type=wb,
    processing_profile=cd4_processing)

viral_load_panel = RequisitionPanel(
    name='vl',
    verbose_name='Viral Load',
    aliquot_type=wb,
    processing_profile=viral_load_processing)

fbc_panel = RequisitionPanel(
    name='fbc',
    verbose_name='Full Blood Count',
    aliquot_type=wb,
    processing_profile=fbc_processing)

chemistry_panel = RequisitionPanel(
    name='chemistry',
    verbose_name='Creat, Urea, Elec',
    aliquot_type=wb,
    processing_profile=chemistry_processing)

chemistry_alt_panel = RequisitionPanel(
    name='chemistry_alt',
    verbose_name='Creat, Urea, Elec, ALT',
    aliquot_type=wb,
    processing_profile=chemistry_alt_processing)

serum_panel = RequisitionPanel(
    name='serum_storage',
    verbose_name='Serum Storage',
    aliquot_type=wb,
    processing_profile=serum_processing)

plasma_buffycoat_panel = RequisitionPanel(
    name='pl_bc_store',
    verbose_name='Plasma and Buffycoat Store',
    aliquot_type=wb,
    processing_profile=plasma_buffycoat_processing)

qpcr_blood_panel = RequisitionPanel(
    name='qpcr',
    verbose_name='qPCR Blood (0hr)',
    aliquot_type=wb,
    processing_profile=qpcr_blood_processing)

qpcr23_blood_panel = RequisitionPanel(
    name='qpcr23',
    verbose_name='qPCR Blood (23hr)',
    aliquot_type=wb,
    processing_profile=qpcr_blood_processing)

pk_plasma_panel_t2 = RequisitionPanel(  # TODO: For Blantyre only
    name='pk_pl_store_t2',
    verbose_name='PK Plasma Store T2',
    aliquot_type=wb,
    processing_profile=plasma_processing)

pk_plasma_panel_t4 = RequisitionPanel(
    name='pk_pl_store_t4',
    verbose_name='PK Plasma Store T4',
    aliquot_type=wb,
    processing_profile=plasma_processing)

pk_plasma_panel_t7 = RequisitionPanel(
    name='pk_pl_store_t7',
    verbose_name='PK Plasma Store T7',
    aliquot_type=wb,
    processing_profile=plasma_processing)

pk_plasma_panel_t12 = RequisitionPanel(
    name='pk_pl_store_t12',
    verbose_name='PK Plasma Store T12',
    aliquot_type=wb,
    processing_profile=plasma_processing)

pk_plasma_panel_t23 = RequisitionPanel(
    name='pk_pl_store_t23',
    verbose_name='PK Plasma Store T23',
    aliquot_type=wb,
    processing_profile=plasma_processing)
