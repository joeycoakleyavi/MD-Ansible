import jmespath

class FilterModule(object):
    def filters(self):
        return {
            'filter_vs': self.filter_vs
        }

    def filter_vs(self, data):
        results = {
            'unique': [],
            'shared': []
        }
        if data.get('obj'):
            vs_data = data['obj']['results']
        else:
          return None

        vsvip_ref_list = [ vip['vsvip_ref'].split('/')[-1] for vip in vs_data ]

        [ results['shared'].append(vsvip_ref) if vsvip_ref_list.count(vsvip_ref) > 1 else \
          results['unique'].append(vsvip_ref) for vsvip_ref in vsvip_ref_list ]


        # Dedupe shared list
        results['shared'] = list(set(results['shared']))


        return results