from hestia_earth.schema import CycleFunctionalUnit, SiteSiteType, TermTermType
from hestia_earth.utils.model import filter_list_term_type, find_term_match
from hestia_earth.utils.tools import list_sum, safe_parse_float
from hestia_earth.utils.lookup import get_table_value, download_lookup, column_name

from ..log import debugRequirements
from .property import get_node_property
from .dataCompleteness import _is_term_type_complete
from .input import get_total_nitrogen
from .measurement import most_relevant_measurement_value
from .site import valid_site_type as site_valid_site_type


def get_excreta_N_total(cycle: dict) -> float:
    """
    Get the total nitrogen content of excreta used in the Cycle.

    The result is the sum of every excreta specified in `kg N` as an `Input` or a `Product`.

    Note: in the event where `dataCompleteness.products` is set to `True` and there are no excreta inputs or products,
    `0` will be returned.

    Parameters
    ----------
    cycle : dict
        The `Cycle` as defined in the Hestia Schema.

    Returns
    -------
    float
        The total value as a number.
    """
    inputs = filter_list_term_type(cycle.get('inputs', []), TermTermType.EXCRETA)
    products = filter_list_term_type(cycle.get('products', []), TermTermType.EXCRETA)
    values = get_total_nitrogen(inputs) + get_total_nitrogen(products)
    return 0 if len(values) == 0 and _is_term_type_complete(cycle, {'termType': 'products'}) else list_sum(values)


def get_max_rooting_depth(cycle: dict) -> float:
    properties = list(map(lambda p: get_node_property(p, 'rootingDepth'), cycle.get('products', [])))
    values = [safe_parse_float(p.get('value')) for p in properties if p.get('value') is not None]
    return max(values) if len(values) > 0 else None


def land_occupation_per_ha(cycle: dict):
    """
    Get the land occupation of the cycle per hectare in hectare.

    Parameters
    ----------
    cycle : dict
        The `Cycle` as defined in the Hestia Schema.

    Returns
    -------
    float
        The land occupation in hectare.
    """
    cycleDuration = cycle.get('cycleDuration', 365)
    fallowCorrection = most_relevant_measurement_value(
        cycle.get('site', {}).get('measurements', []), 'fallowCorrection', cycle.get('endDate')) or 1
    value = cycleDuration / 365 * fallowCorrection
    debugRequirements(term='landOccupation',
                      cycleDuration=cycleDuration,
                      fallowCorrection=fallowCorrection,
                      value_per_ha=value)
    return value


def _orchard_crop_land_occupation_per_ha(cycle: dict):
    practices = cycle.get('practices', [])
    nurseryDuration = list_sum(find_term_match(practices, 'nurseryDuration').get('value', [0]))
    orchardBearingDuration = list_sum(find_term_match(practices, 'orchardBearingDuration').get('value', [0]))
    orchardDensity = list_sum(find_term_match(practices, 'orchardDensity').get('value', [0]))
    orchardDuration = list_sum(find_term_match(practices, 'orchardDuration').get('value', [0]))
    rotationDuration = list_sum(find_term_match(practices, 'rotationDuration').get('value', [0]))
    saplings = list_sum(find_term_match(cycle.get('inputs', []), 'saplings').get('value', [0]))
    debugRequirements(term='landOccupation',
                      nurseryDuration=nurseryDuration,
                      saplings=saplings,
                      orchardDensity=orchardDensity,
                      orchardDuration=orchardDuration,
                      orchardBearingDuration=orchardBearingDuration,
                      rotationDuration=rotationDuration)
    should_run = all([
        nurseryDuration, saplings, orchardDensity, orchardDuration, orchardBearingDuration, rotationDuration
    ])
    return (orchardDuration/orchardBearingDuration) * (
        1 + (nurseryDuration/365)/saplings * orchardDensity/(orchardDuration/365)  # nursery
    ) * rotationDuration/orchardDuration if should_run else None


def land_occupation_per_kg(cycle: dict, primary_product: dict):
    """
    Get the land occupation of the cycle per kg in meter square.

    Parameters
    ----------
    cycle : dict
        The `Cycle` as defined in the Hestia Schema.
    product : dict
        The primary `Product` of the `Cycle`.

    Returns
    -------
    float
        The land occupation in m2.
    """
    functionalUnit = cycle.get('functionalUnit')
    product_value = list_sum(primary_product.get('value', [0]))
    economicValueShare = primary_product.get('economicValueShare', 0)

    value = _orchard_crop_land_occupation_per_ha(cycle) or land_occupation_per_ha(cycle)
    value = value * 10000 * (economicValueShare / 100)
    value = value / product_value if product_value > 0 else None
    # TODO: handle relative unit
    value = value if functionalUnit == CycleFunctionalUnit._1_HA.value else None
    debugRequirements(term='landOccupation',
                      functionalUnit=functionalUnit,
                      product_yield=product_value,
                      economicValueShare=economicValueShare,
                      value_per_kg_per_m2=value)
    return value


def valid_site_type(cycle: dict, include_permanent_pasture=False):
    """
    Check if the `site.siteType` of the cycle is `cropland`.

    Parameters
    ----------
    cycle : dict
        The `Cycle`.
    include_permanent_pasture : bool
        If set to `True`, `permanent pasture` is also allowed. Defaults to `False`.

    Returns
    -------
    bool
        `True` if `siteType` matches the allowed values, `False` otherwise.
    """
    site_types = [SiteSiteType.CROPLAND.value] + (
        [SiteSiteType.PERMANENT_PASTURE.value] if include_permanent_pasture else []
    )
    return site_valid_site_type(cycle.get('site', {}), site_types)


def is_organic(cycle: dict):
    """
    Check if the `Cycle` is organic, i.e. if it contains an organic `Practice`.

    Parameters
    ----------
    cycle : dict
        The `Cycle`.

    Returns
    -------
    bool
        `True` if the `Cycle` is organic, `False` otherwise.
    """
    lookup = download_lookup('standardsLabels.csv')

    def term_organic(lookup, term_id: str):
        return get_table_value(lookup, 'termid', term_id, column_name('isOrganic')) == 'organic'

    practices = list(filter(lambda p: p.get('term') is not None, cycle.get('practices', [])))
    return any([term_organic(lookup, p.get('term', {}).get('@id')) for p in practices])


def is_irrigated(cycle: dict):
    """
    Check if the `Cycle` is irrigated, i.e. if it contains an irrigated `Practice`.

    Parameters
    ----------
    cycle : dict
        The `Cycle`.

    Returns
    -------
    bool
        `True` if the `Cycle` is irrigated, `False` otherwise.
    """
    practices = cycle.get('practices', [])
    return next((p for p in practices if p.get('term', {}).get('@id') == 'irrigated'), None) is not None
