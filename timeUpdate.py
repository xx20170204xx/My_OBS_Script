
import obspython as obs
import datetime

source_name = ""
g_time_fmt = "%Y-%m-%d %H:%M:%S"

# ------------------------------------------------------------


def refresh_pressed(props, prop):
    print("Refresh Pressed")

    update_text()


def update_text():
    global source_name

    source = obs.obs_get_source_by_name(source_name)
    text = ""
    if source is not None:
        settings = obs.obs_data_create()
        text = datetime.datetime.now().strftime(g_time_fmt)
        obs.obs_data_set_string(settings, "text", text)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)

# ------------------------------------------------------------


def script_properties():
    props = obs.obs_properties_create()
    p = obs.obs_properties_add_list(props, "source", "Text Source",
                                    obs.OBS_COMBO_TYPE_EDITABLE,
                                    obs.OBS_COMBO_FORMAT_STRING)
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_id(source)
            if source_id == "text_gdiplus" or source_id == "text_ft2_source":
                name = obs.obs_source_get_name(source)
                obs.obs_property_list_add_string(p, name, name)

        obs.source_list_release(sources)

    obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
    obs.obs_properties_add_int(props,
                               "update_rate",
                               "Update Rate(ms)",
                               1000,
                               10000,
                               1)

    fmt_list = obs.obs_properties_add_list(props, "format", "Format", 
                                    obs.OBS_COMBO_TYPE_EDITABLE,
                                    obs.OBS_COMBO_FORMAT_STRING)
    fmt = "%Y-%m-%d %H:%M:%S"
    obs.obs_property_list_add_string(fmt_list, fmt, fmt)

    fmt = "%m-%d %H:%M:%S"
    obs.obs_property_list_add_string(fmt_list, fmt, fmt)

    fmt = "%H:%M:%S"
    obs.obs_property_list_add_string(fmt_list, fmt, fmt)

    return props


def script_update(settings):

    global source_name
    global g_time_fmt

    source_name = obs.obs_data_get_string(settings, "source")
    update_rate = obs.obs_data_get_int(settings, "update_rate")
    g_time_fmt = obs.obs_data_get_string(settings, "format")
    obs.timer_add(update_text, update_rate)
