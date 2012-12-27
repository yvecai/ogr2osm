"""
Translation rules for fire hydrants

"""

def filterTags(attrs):
	if not attrs: return
	
	tags = {}
	
	if attrs['EMERGENCY'] == 'fire_hydrant':
		tags.update({'emergency':'fire_hydrant'})
	if attrs['REF']:
		tags.update({'ref':attrs['REF']})
	if attrs['FIRE_HYDRA']:
		tags.update({'fire_hydrant:type':attrs['FIRE_HYDRA']})
	if attrs['ES_T_SOUPA']:
		tags.update({'fire_hydrant:diameter':attrs['ES_D_SOUPA']})
	if attrs['PRESSION_S']:
		tags.update({'fire_hydrant:pressure':attrs['PRESSION_S']})
	if attrs['ES_SITUATI']:
		tags.update({'fire_hydrant:position':attrs['ES_SITUATI']})
	
	if attrs['SOURCE']:
		tags.update({'source':attrs['SOURCE']})
	else:
		tags.update({'source':'eauservice_2012-12'})
	
	return tags


