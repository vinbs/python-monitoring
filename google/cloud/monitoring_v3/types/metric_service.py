# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.api import metric_pb2 as ga_metric  # type: ignore
from google.api import monitored_resource_pb2 as monitored_resource  # type: ignore
from google.cloud.monitoring_v3.types import common
from google.cloud.monitoring_v3.types import metric as gm_metric
from google.rpc import status_pb2 as gr_status  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.monitoring.v3",
    manifest={
        "ListMonitoredResourceDescriptorsRequest",
        "ListMonitoredResourceDescriptorsResponse",
        "GetMonitoredResourceDescriptorRequest",
        "ListMetricDescriptorsRequest",
        "ListMetricDescriptorsResponse",
        "GetMetricDescriptorRequest",
        "CreateMetricDescriptorRequest",
        "DeleteMetricDescriptorRequest",
        "ListTimeSeriesRequest",
        "ListTimeSeriesResponse",
        "CreateTimeSeriesRequest",
        "CreateTimeSeriesError",
        "CreateTimeSeriesSummary",
        "QueryTimeSeriesRequest",
        "QueryTimeSeriesResponse",
        "QueryErrorList",
    },
)


class ListMonitoredResourceDescriptorsRequest(proto.Message):
    r"""The ``ListMonitoredResourceDescriptors`` request.

    Attributes:
        name (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        filter (str):
            An optional
            `filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            describing the descriptors to be returned. The filter can
            reference the descriptor's type and labels. For example, the
            following filter returns only Google Compute Engine
            descriptors that have an ``id`` label:

            ::

                resource.type = starts_with("gce_") AND resource.label:id
        page_size (int):
            A positive number that is the maximum number
            of results to return.
        page_token (str):
            If this field is not empty then it must contain the
            ``nextPageToken`` value returned by a previous call to this
            method. Using this field causes the method to return
            additional results from the previous method call.
    """

    name = proto.Field(proto.STRING, number=5)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)


class ListMonitoredResourceDescriptorsResponse(proto.Message):
    r"""The ``ListMonitoredResourceDescriptors`` response.

    Attributes:
        resource_descriptors (Sequence[~.monitored_resource.MonitoredResourceDescriptor]):
            The monitored resource descriptors that are available to
            this project and that match ``filter``, if present.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
    """

    @property
    def raw_page(self):
        return self

    resource_descriptors = proto.RepeatedField(
        proto.MESSAGE, number=1, message=monitored_resource.MonitoredResourceDescriptor,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class GetMonitoredResourceDescriptorRequest(proto.Message):
    r"""The ``GetMonitoredResourceDescriptor`` request.

    Attributes:
        name (str):
            Required. The monitored resource descriptor to get. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]/monitoredResourceDescriptors/[RESOURCE_TYPE]

            The ``[RESOURCE_TYPE]`` is a predefined type, such as
            ``cloudsql_database``.
    """

    name = proto.Field(proto.STRING, number=3)


class ListMetricDescriptorsRequest(proto.Message):
    r"""The ``ListMetricDescriptors`` request.

    Attributes:
        name (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        filter (str):
            If this field is empty, all custom and system-defined metric
            descriptors are returned. Otherwise, the
            `filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            specifies which metric descriptors are to be returned. For
            example, the following filter matches all `custom
            metrics <https://cloud.google.com/monitoring/custom-metrics>`__:

            ::

                metric.type = starts_with("custom.googleapis.com/")
        page_size (int):
            A positive number that is the maximum number
            of results to return.
        page_token (str):
            If this field is not empty then it must contain the
            ``nextPageToken`` value returned by a previous call to this
            method. Using this field causes the method to return
            additional results from the previous method call.
    """

    name = proto.Field(proto.STRING, number=5)

    filter = proto.Field(proto.STRING, number=2)

    page_size = proto.Field(proto.INT32, number=3)

    page_token = proto.Field(proto.STRING, number=4)


class ListMetricDescriptorsResponse(proto.Message):
    r"""The ``ListMetricDescriptors`` response.

    Attributes:
        metric_descriptors (Sequence[~.ga_metric.MetricDescriptor]):
            The metric descriptors that are available to the project and
            that match the value of ``filter``, if present.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
    """

    @property
    def raw_page(self):
        return self

    metric_descriptors = proto.RepeatedField(
        proto.MESSAGE, number=1, message=ga_metric.MetricDescriptor,
    )

    next_page_token = proto.Field(proto.STRING, number=2)


class GetMetricDescriptorRequest(proto.Message):
    r"""The ``GetMetricDescriptor`` request.

    Attributes:
        name (str):
            Required. The metric descriptor on which to execute the
            request. The format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]/metricDescriptors/[METRIC_ID]

            An example value of ``[METRIC_ID]`` is
            ``"compute.googleapis.com/instance/disk/read_bytes_count"``.
    """

    name = proto.Field(proto.STRING, number=3)


class CreateMetricDescriptorRequest(proto.Message):
    r"""The ``CreateMetricDescriptor`` request.

    Attributes:
        name (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        metric_descriptor (~.ga_metric.MetricDescriptor):
            Required. The new `custom
            metric <https://cloud.google.com/monitoring/custom-metrics>`__
            descriptor.
    """

    name = proto.Field(proto.STRING, number=3)

    metric_descriptor = proto.Field(
        proto.MESSAGE, number=2, message=ga_metric.MetricDescriptor,
    )


class DeleteMetricDescriptorRequest(proto.Message):
    r"""The ``DeleteMetricDescriptor`` request.

    Attributes:
        name (str):
            Required. The metric descriptor on which to execute the
            request. The format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]/metricDescriptors/[METRIC_ID]

            An example of ``[METRIC_ID]`` is:
            ``"custom.googleapis.com/my_test_metric"``.
    """

    name = proto.Field(proto.STRING, number=3)


class ListTimeSeriesRequest(proto.Message):
    r"""The ``ListTimeSeries`` request.

    Attributes:
        name (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        filter (str):
            Required. A `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            that specifies which time series should be returned. The
            filter must specify a single metric type, and can
            additionally specify metric labels and other information.
            For example:

            ::

                metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
                    metric.labels.instance_name = "my-instance-name".
        interval (~.common.TimeInterval):
            Required. The time interval for which results
            should be returned. Only time series that
            contain data points in the specified interval
            are included in the response.
        aggregation (~.common.Aggregation):
            Specifies the alignment of data points in individual time
            series as well as how to combine the retrieved time series
            across specified labels.

            By default (if no ``aggregation`` is explicitly specified),
            the raw time series data is returned.
        order_by (str):
            Unsupported: must be left blank. The points
            in each time series are currently returned in
            reverse time order (most recent to oldest).
        view (~.metric_service.ListTimeSeriesRequest.TimeSeriesView):
            Required. Specifies which information is
            returned about the time series.
        page_size (int):
            A positive number that is the maximum number of results to
            return. If ``page_size`` is empty or more than 100,000
            results, the effective ``page_size`` is 100,000 results. If
            ``view`` is set to ``FULL``, this is the maximum number of
            ``Points`` returned. If ``view`` is set to ``HEADERS``, this
            is the maximum number of ``TimeSeries`` returned.
        page_token (str):
            If this field is not empty then it must contain the
            ``nextPageToken`` value returned by a previous call to this
            method. Using this field causes the method to return
            additional results from the previous method call.
    """

    class TimeSeriesView(proto.Enum):
        r"""Controls which fields are returned by ``ListTimeSeries``."""
        FULL = 0
        HEADERS = 1

    name = proto.Field(proto.STRING, number=10)

    filter = proto.Field(proto.STRING, number=2)

    interval = proto.Field(proto.MESSAGE, number=4, message=common.TimeInterval,)

    aggregation = proto.Field(proto.MESSAGE, number=5, message=common.Aggregation,)

    order_by = proto.Field(proto.STRING, number=6)

    view = proto.Field(proto.ENUM, number=7, enum=TimeSeriesView,)

    page_size = proto.Field(proto.INT32, number=8)

    page_token = proto.Field(proto.STRING, number=9)


class ListTimeSeriesResponse(proto.Message):
    r"""The ``ListTimeSeries`` response.

    Attributes:
        time_series (Sequence[~.gm_metric.TimeSeries]):
            One or more time series that match the filter
            included in the request.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
        execution_errors (Sequence[~.gr_status.Status]):
            Query execution errors that may have caused
            the time series data returned to be incomplete.
    """

    @property
    def raw_page(self):
        return self

    time_series = proto.RepeatedField(
        proto.MESSAGE, number=1, message=gm_metric.TimeSeries,
    )

    next_page_token = proto.Field(proto.STRING, number=2)

    execution_errors = proto.RepeatedField(
        proto.MESSAGE, number=3, message=gr_status.Status,
    )


class CreateTimeSeriesRequest(proto.Message):
    r"""The ``CreateTimeSeries`` request.

    Attributes:
        name (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        time_series (Sequence[~.gm_metric.TimeSeries]):
            Required. The new data to be added to a list of time series.
            Adds at most one data point to each of several time series.
            The new data point must be more recent than any other point
            in its time series. Each ``TimeSeries`` value must fully
            specify a unique time series by supplying all label values
            for the metric and the monitored resource.

            The maximum number of ``TimeSeries`` objects per ``Create``
            request is 200.
    """

    name = proto.Field(proto.STRING, number=3)

    time_series = proto.RepeatedField(
        proto.MESSAGE, number=2, message=gm_metric.TimeSeries,
    )


class CreateTimeSeriesError(proto.Message):
    r"""DEPRECATED. Used to hold per-time-series error status.

    Attributes:
        time_series (~.gm_metric.TimeSeries):
            DEPRECATED. Time series ID that resulted in the ``status``
            error.
        status (~.gr_status.Status):
            DEPRECATED. The status of the requested write operation for
            ``time_series``.
    """

    time_series = proto.Field(proto.MESSAGE, number=1, message=gm_metric.TimeSeries,)

    status = proto.Field(proto.MESSAGE, number=2, message=gr_status.Status,)


class CreateTimeSeriesSummary(proto.Message):
    r"""Summary of the result of a failed request to write data to a
    time series.

    Attributes:
        total_point_count (int):
            The number of points in the request.
        success_point_count (int):
            The number of points that were successfully
            written.
        errors (Sequence[~.metric_service.CreateTimeSeriesSummary.Error]):
            The number of points that failed to be
            written. Order is not guaranteed.
    """

    class Error(proto.Message):
        r"""Detailed information about an error category.

        Attributes:
            status (~.gr_status.Status):
                The status of the requested write operation.
            point_count (int):
                The number of points that couldn't be written because of
                ``status``.
        """

        status = proto.Field(proto.MESSAGE, number=1, message=gr_status.Status,)

        point_count = proto.Field(proto.INT32, number=2)

    total_point_count = proto.Field(proto.INT32, number=1)

    success_point_count = proto.Field(proto.INT32, number=2)

    errors = proto.RepeatedField(proto.MESSAGE, number=3, message=Error,)


class QueryTimeSeriesRequest(proto.Message):
    r"""The ``QueryTimeSeries`` request.

    Attributes:
        name (str):
            Required. The project on which to execute the request. The
            format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]
        query (str):
            Required. The query in the monitoring query
            language format. The default time zone is in
            UTC.
        page_size (int):
            A positive number that is the maximum number of
            time_series_data to return.
        page_token (str):
            If this field is not empty then it must contain the
            ``nextPageToken`` value returned by a previous call to this
            method. Using this field causes the method to return
            additional results from the previous method call.
    """

    name = proto.Field(proto.STRING, number=1)

    query = proto.Field(proto.STRING, number=7)

    page_size = proto.Field(proto.INT32, number=9)

    page_token = proto.Field(proto.STRING, number=10)


class QueryTimeSeriesResponse(proto.Message):
    r"""The ``QueryTimeSeries`` response.

    Attributes:
        time_series_descriptor (~.gm_metric.TimeSeriesDescriptor):
            The descriptor for the time series data.
        time_series_data (Sequence[~.gm_metric.TimeSeriesData]):
            The time series data.
        next_page_token (str):
            If there are more results than have been returned, then this
            field is set to a non-empty value. To see the additional
            results, use that value as ``page_token`` in the next call
            to this method.
        partial_errors (Sequence[~.gr_status.Status]):
            Query execution errors that may have caused
            the time series data returned to be incomplete.
            The available data will be available in the
            response.
    """

    @property
    def raw_page(self):
        return self

    time_series_descriptor = proto.Field(
        proto.MESSAGE, number=8, message=gm_metric.TimeSeriesDescriptor,
    )

    time_series_data = proto.RepeatedField(
        proto.MESSAGE, number=9, message=gm_metric.TimeSeriesData,
    )

    next_page_token = proto.Field(proto.STRING, number=10)

    partial_errors = proto.RepeatedField(
        proto.MESSAGE, number=11, message=gr_status.Status,
    )


class QueryErrorList(proto.Message):
    r"""This is an error detail intended to be used with INVALID_ARGUMENT
    errors.

    Attributes:
        errors (Sequence[~.gm_metric.QueryError]):
            Errors in parsing the time series query
            language text. The number of errors in the
            response may be limited.
        error_summary (str):
            A summary of all the errors.
    """

    errors = proto.RepeatedField(proto.MESSAGE, number=1, message=gm_metric.QueryError,)

    error_summary = proto.Field(proto.STRING, number=2)


__all__ = tuple(sorted(__protobuf__.manifest))