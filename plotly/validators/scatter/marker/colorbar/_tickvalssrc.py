import _plotly_utils.basevalidators


class TickvalssrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self,
        plotly_name='tickvalssrc',
        parent_name='scatter.marker.colorbar',
        **kwargs
    ):
        super(TickvalssrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )