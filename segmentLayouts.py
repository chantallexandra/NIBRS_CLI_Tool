from segments.federalAdministrative import FederalAdminSegment
from segments.federalOffense import FederalOffenseSegment
from segments.federalProperty import FederalPropertySegment
from segments.federalVictim import FederalVictimSegment
from segments.federalOffender import FederalOffenderSegment
from segments.federalArrestee import FederalArresteeSegment
from segments.federalGroupBArrest import FederalGroupBSegment
from segments.federalZeroReport import FederalZeroReportSegment
from segments.pennsylvaniaSegment8 import PennsylvaniaSegment8
from segments.pennsylvaniaSegment9 import PennsylvaniaSegment9
from segments.pennsylvaniaSegment10 import PennsylvaniaSegment10
from segments.californiaSegment8 import CaliforniaSegment8
from segments.californiaSegment9 import CaliforniaSegment9
from segments.californiaSegmentA import CaliforniaSegmentA
from segments.californiaSegmentB import CaliforniaSegmentB
from segments.texasSegment8 import TexasSegment8
from segments.texasSegment9 import TexasSegment9

segment_layouts = {
			"0": FederalZeroReportSegment,
			"1": FederalAdminSegment,
			"2": FederalOffenseSegment, 
			"3": FederalPropertySegment,
			"4": FederalVictimSegment,
			"5": FederalOffenderSegment,
			"6": FederalArresteeSegment,
			"7": FederalGroupBSegment,
			"8": [{"state": "PA", "segment": PennsylvaniaSegment8}, {"state": "CA", "segment": CaliforniaSegment8}, {"state": "TX", "segment": TexasSegment8}],
			"9": [{"state": "PA", "segment": PennsylvaniaSegment9}, {"state": "CA", "segment": CaliforniaSegment9}, {"state": "TX", "segment": TexasSegment9}],
			"A": [{"state": "PA", "segment": PennsylvaniaSegment10}, {"state": "CA", "segment": CaliforniaSegmentA}],
			"B": [{"state": "CA", "segment": CaliforniaSegmentB}]
		}
