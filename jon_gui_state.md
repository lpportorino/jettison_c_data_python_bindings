# jon_gui_state Structure Documentation

This document describes the complete structure of the `jon_gui_state` data type.
This structure is used for sharing GUI state data between components.

## Structure: struct_jon_gui_state

- **`header`** : `struct_jon_gui_data_header`
  ### struct_jon_gui_data_header
  - **`version`** : `int32`
  - **`state_update_counter`** : `int32`
  - **`system_monotonic_time_us`** : `uint64`
  - **`unnamed_1`** : `union_anon_13`
    ### union_anon_13
    - **`active_mode_id`** : `int32`
    - **`active_mode_id_packed`** : `int32`
  - **`unnamed_2`** : `union_anon_14`
    ### union_anon_14
    - **`active_screen_id`** : `int32`
    - **`active_screen_id_packed`** : `int32`
- **`compass`** : `struct_jon_gui_data_compass`
  ### struct_jon_gui_data_compass
  - **`azimuth`** : `int32`
  - **`elevation`** : `int32`
  - **`bank`** : `int32`
  - **`offset`** : `int32`
  - **`unnamed_1`** : `union_anon_4`
    ### union_anon_4
    - **`units_idx`** : `int32`
    - **`units_idx_packed`** : `int32`
  - **`unnamed_2`** : `union_anon_5`
    ### union_anon_5
    - **`device_status`** : `int32`
    - **`device_status_packed`** : `int32`
  - **`meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
- **`compass_calibration`** : `struct_jon_gui_data_compass_calibration`
  ### struct_jon_gui_data_compass_calibration
  - **`stage`** : `int32`
  - **`final_stage`** : `int32`
  - **`target_azimuth`** : `int32`
  - **`target_elevation`** : `int32`
  - **`target_bank`** : `int32`
  - **`unnamed_1`** : `union_anon_6`
    ### union_anon_6
    - **`status`** : `int32`
    - **`jon_gui_data_compass_calibrate_status_packed`** : `int32`
- **`colors`** : `struct_jon_gui_data_colors`
  ### struct_jon_gui_data_colors
  - **`menu`** : `struct_jon_gui_data_colors_menu`
    ### struct_jon_gui_data_colors_menu
    - **`bg`** : `struct_jon_gui_data_colors_value`
      ### struct_jon_gui_data_colors_value
      - **`h`** : `int32`
      - **`s`** : `int32`
      - **`v`** : `int32`
      - **`a`** : `int32`
    - **`text`** : `struct_jon_gui_data_colors_value`
      ### struct_jon_gui_data_colors_value
      - **`h`** : `int32`
      - **`s`** : `int32`
      - **`v`** : `int32`
      - **`a`** : `int32`
    - **`focused`** : `struct_jon_gui_data_colors_value`
      ### struct_jon_gui_data_colors_value
      - **`h`** : `int32`
      - **`s`** : `int32`
      - **`v`** : `int32`
      - **`a`** : `int32`
  - **`osd`** : `struct_jon_gui_data_colors_osd`
    ### struct_jon_gui_data_colors_osd
    - **`main`** : `struct_jon_gui_data_colors_value`
      ### struct_jon_gui_data_colors_value
      - **`h`** : `int32`
      - **`s`** : `int32`
      - **`v`** : `int32`
      - **`a`** : `int32`
    - **`accent`** : `struct_jon_gui_data_colors_value`
      ### struct_jon_gui_data_colors_value
      - **`h`** : `int32`
      - **`s`** : `int32`
      - **`v`** : `int32`
      - **`a`** : `int32`
    - **`faded`** : `struct_jon_gui_data_colors_value`
      ### struct_jon_gui_data_colors_value
      - **`h`** : `int32`
      - **`s`** : `int32`
      - **`v`** : `int32`
      - **`a`** : `int32`
- **`time`** : `struct_jon_gui_data_time`
  ### struct_jon_gui_data_time
  - **`unnamed_1`** : `union_anon_34`
    ### union_anon_34
    - **`timestamp`** : `int64`
    - **`unnamed_1`** : `struct_anon_33`
      ### struct_anon_33
      - **`timestamp_low`** : `int32`
      - **`timestamp_hi`** : `int32`
  - **`unnamed_2`** : `union_anon_36`
    ### union_anon_36
    - **`manual_timestamp`** : `int64`
    - **`unnamed_1`** : `struct_anon_35`
      ### struct_anon_35
      - **`manual_timestamp_low`** : `int32`
      - **`manual_timestamp_hi`** : `int32`
  - **`zone_id`** : `int32`
  - **`use_manual_time`** : `int32`
- **`gps`** : `struct_jon_gui_data_gps`
  ### struct_jon_gui_data_gps
  - **`longitude`** : `int32`
  - **`latitude`** : `int32`
  - **`height`** : `int32`
  - **`manual_longitude`** : `int32`
  - **`manual_latitude`** : `int32`
  - **`manual_altitude`** : `int32`
  - **`unnamed_1`** : `union_anon_9`
    ### union_anon_9
    - **`timestamp`** : `int64`
    - **`unnamed_1`** : `struct_anon_8`
      ### struct_anon_8
      - **`timestamp_low`** : `int32`
      - **`timestamp_hi`** : `int32`
  - **`unnamed_2`** : `union_anon_10`
    ### union_anon_10
    - **`fix_type`** : `int32`
    - **`fix_type_packed`** : `int32`
  - **`use_manual`** : `int32`
  - **`unnamed_3`** : `union_anon_11`
    ### union_anon_11
    - **`units_idx`** : `int32`
    - **`units_packed`** : `int32`
  - **`unnamed_4`** : `union_anon_12`
    ### union_anon_12
    - **`device_status`** : `int32`
    - **`device_status_packed`** : `int32`
  - **`meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
- **`lrf`** : `struct_jon_gui_data_lrf`
  ### struct_jon_gui_data_lrf
  - **`scanning`** : `int32`
  - **`measuring`** : `int32`
  - **`refining`** : `int32`
  - **`last_range_measured_val_1`** : `int32`
  - **`last_range_measured_val_2`** : `int32`
  - **`last_range_measured_val_3`** : `int32`
  - **`fog_mode_enabled`** : `int32`
  - **`scanning_mode_freq`** : `int32`
  - **`measure_id`** : `int32`
  - **`unnamed_1`** : `union_anon_19`
    ### union_anon_19
    - **`target_designator_status`** : `int32`
    - **`target_designator_status_packed`** : `int32`
  - **`error_bf`** : `int32`
  - **`unnamed_2`** : `union_anon_20`
    ### union_anon_20
    - **`device_status`** : `int32`
    - **`device_status_packed`** : `int32`
  - **`meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
- **`media`** : `struct_jon_gui_data_media`
  ### struct_jon_gui_data_media
  - **`space_left_prc`** : `int32`
- **`system`** : `struct_jon_gui_data_system`
  ### struct_jon_gui_data_system
  - **`enable_video_recording`** : `int32`
  - **`recording_is_important`** : `int32`
  - **`disk_space_percent_taken`** : `int32`
  - **`day_af_enable`** : `int32`
  - **`day_ae_enable`** : `int32`
  - **`day_air_enable`** : `int32`
  - **`heat_af_enable`** : `int32`
  - **`heat_filter_value`** : `int32`
  - **`irf_enable`** : `int32`
  - **`is_enable`** : `int32`
  - **`agc_mode`** : `int32`
  - **`enable_zoom_sync`** : `int32`
  - **`eth_enabled`** : `int32`
  - **`wifi_enabled`** : `int32`
  - **`enable_continuous_zoom`** : `int32`
  - **`shutdown_timer_running`** : `int32`
  - **`geodesic_mode_enabled`** : `int32`
  - **`unnamed_1`** : `union_anon_25`
    ### union_anon_25
    - **`localization_id`** : `int32`
    - **`localization_id_packed`** : `int32`
  - **`unnamed_2`** : `union_anon_26`
    ### union_anon_26
    - **`active_video_channel`** : `int32`
    - **`active_video_channel_packed`** : `int32`
  - **`unnamed_3`** : `union_anon_27`
    ### union_anon_27
    - **`active_thermal_color_filter_idx`** : `int32`
    - **`active_thermal_color_filter_packed`** : `int32`
  - **`unnamed_4`** : `union_anon_28`
    ### union_anon_28
    - **`active_day_filter_idx`** : `int32`
    - **`active_day_filter_packed`** : `int32`
  - **`unnamed_5`** : `union_anon_29`
    ### union_anon_29
    - **`acccumulator_stat_idx`** : `int32`
    - **`acccumulator_stat_idx_packed`** : `int32`
  - **`unnamed_6`** : `union_anon_30`
    ### union_anon_30
    - **`sd_card_stat_idx`** : `int32`
    - **`sd_card_stat_idx_packed`** : `int32`
  - **`cur_video_rec_dir_year`** : `int32`
  - **`cur_video_rec_dir_month`** : `int32`
  - **`cur_video_rec_dir_day`** : `int32`
  - **`cur_video_rec_dir_hour`** : `int32`
  - **`cur_video_rec_dir_minute`** : `int32`
  - **`cur_video_rec_dir_second`** : `int32`
  - **`low_disk_space`** : `int32`
  - **`no_disk_space`** : `int32`
- **`osd`** : `struct_jon_gui_data_osd`
  ### struct_jon_gui_data_osd
  - **`show_on_recording`** : `int32`
  - **`crosshair_index`** : `int32`
  - **`crosshair_size_indx`** : `int32`
  - **`faded_opa`** : `int32`
  - **`fade_enabled`** : `int32`
  - **`show_photo_indicator`** : `int32`
  - **`disable_heat_osd`** : `int32`
  - **`disable_day_osd`** : `int32`
  - **`unnamed_1`** : `union_anon_21`
    ### union_anon_21
    - **`pip_pos_id`** : `int32`
    - **`pip_pos_id_packed`** : `int32`
- **`targets`** : `struct_jon_gui_data_targets`
  ### struct_jon_gui_data_targets
  - **`last_target`** : `struct_jon_gui_data_target_spec`
    ### struct_jon_gui_data_target_spec
    - **`target_id`** : `int32`
    - **`target_index`** : `int32`
    - **`uuid`** : `int32[4]` [array of 4]
    - **`target_longitude`** : `int32`
    - **`target_latitude`** : `int32`
    - **`target_height`** : `int32`
    - **`observer_id`** : `int32`
    - **`unnamed_1`** : `union_anon_31`
      ### union_anon_31
      - **`observer_timestamp`** : `int64`
      - **`observer_timestamp_packed`** : `int64`
    - **`observer_longitude`** : `int32`
    - **`observer_latitude`** : `int32`
    - **`observer_azimuth`** : `int32`
    - **`observer_elevation`** : `int32`
    - **`observer_altitude`** : `int32`
    - **`distance_a`** : `int32`
    - **`distance_b`** : `int32`
    - **`has_range`** : `int32`
    - **`session_id`** : `int32`
    - **`unnamed_2`** : `union_anon_32`
      ### union_anon_32
      - **`observer_fix_type`** : `int32`
      - **`observer_fix_type_packed`** : `int32`
  - **`target_viewr_current_target`** : `struct_jon_gui_data_target_spec`
    ### struct_jon_gui_data_target_spec
    - **`target_id`** : `int32`
    - **`target_index`** : `int32`
    - **`uuid`** : `int32[4]` [array of 4]
    - **`target_longitude`** : `int32`
    - **`target_latitude`** : `int32`
    - **`target_height`** : `int32`
    - **`observer_id`** : `int32`
    - **`unnamed_1`** : `union_anon_31`
      ### union_anon_31
      - **`observer_timestamp`** : `int64`
      - **`observer_timestamp_packed`** : `int64`
    - **`observer_longitude`** : `int32`
    - **`observer_latitude`** : `int32`
    - **`observer_azimuth`** : `int32`
    - **`observer_elevation`** : `int32`
    - **`observer_altitude`** : `int32`
    - **`distance_a`** : `int32`
    - **`distance_b`** : `int32`
    - **`has_range`** : `int32`
    - **`session_id`** : `int32`
    - **`unnamed_2`** : `union_anon_32`
      ### union_anon_32
      - **`observer_fix_type`** : `int32`
      - **`observer_fix_type_packed`** : `int32`
  - **`recorded_targets_count`** : `int32`
  - **`screenshot_state`** : `int32`
- **`camera_alignment`** : `struct_jon_gui_data_camera_alignment`
  ### struct_jon_gui_data_camera_alignment
  - **`table_row`** : `int32`
  - **`day_focus_target_pos`** : `int32`
  - **`heat_focus_target_pos`** : `int32`
  - **`day_zoom_target_pos`** : `int32`
  - **`heat_zoom_target_pos`** : `int32`
  - **`day_cross_hair_offset_ver`** : `int32`
  - **`heat_cross_hair_offset_ver`** : `int32`
  - **`day_cross_hair_offset_hor`** : `int32`
  - **`heat_cross_hair_offset_hor`** : `int32`
  - **`used`** : `int32`
- **`meteo`** : `struct_jon_gui_data_meteo`
  ### struct_jon_gui_data_meteo
  - **`internal_temperature`** : `int32`
  - **`internal_humidity`** : `int32`
  - **`internal_pressure`** : `int32`
  - **`external_temperature`** : `int32`
  - **`external_humidity`** : `int32`
  - **`external_pressure`** : `int32`
- **`lens`** : `struct_jon_gui_data_lens`
  ### struct_jon_gui_data_lens
  - **`day_focus_pos`** : `int32`
  - **`day_focus_pos_min`** : `int32`
  - **`day_focus_pos_max`** : `int32`
  - **`day_zoom_table_index`** : `int32`
  - **`day_zoom_table_max_index`** : `int32`
  - **`heat_zoom_table_index`** : `int32`
  - **`heat_zoom_table_max_index`** : `int32`
  - **`heat_focus_pos`** : `int32`
  - **`day_zoom_pos`** : `int32`
  - **`day_glass_temperature`** : `int32`
  - **`day_glass_heater_enabled`** : `int32`
  - **`day_meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
  - **`day_glass_heater_meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
  - **`heat_meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
  - **`day_zoom_pos_min`** : `int32`
  - **`day_zoom_pos_max`** : `int32`
  - **`heat_zoom_pos`** : `int32`
  - **`day_zoom_x`** : `int32`
  - **`heat_zoom_x`** : `int32`
  - **`day_iris_pos`** : `int32`
  - **`day_crop_top`** : `int32`
  - **`day_crop_bottom`** : `int32`
  - **`day_crop_left`** : `int32`
  - **`day_crop_right`** : `int32`
  - **`heat_iris_pos`** : `int32`
  - **`heat_crop_top`** : `int32`
  - **`heat_crop_bottom`** : `int32`
  - **`heat_crop_left`** : `int32`
  - **`heat_crop_right`** : `int32`
  - **`heat_dde_enabled`** : `int32`
  - **`heat_dde_level`** : `int32`
  - **`heat_dde_max_level`** : `int32`
  - **`day_digital_zoom_level`** : `int32`
  - **`heat_digital_zoom_level`** : `int32`
  - **`day_clahe_level`** : `int32`
  - **`heat_clahe_level`** : `int32`
  - **`unnamed_1`** : `union_anon_15`
    ### union_anon_15
    - **`device_status_day`** : `int32`
    - **`device_status_day_packed`** : `int32`
  - **`unnamed_2`** : `union_anon_16`
    ### union_anon_16
    - **`device_status_heat`** : `int32`
    - **`device_status_heat_packed`** : `int32`
  - **`unnamed_3`** : `union_anon_17`
    ### union_anon_17
    - **`fx_mode_day`** : `int32`
    - **`fx_mode_day_packed`** : `int32`
  - **`unnamed_4`** : `union_anon_18`
    ### union_anon_18
    - **`fx_mode_heat`** : `int32`
    - **`fx_mode_heat_packed`** : `int32`
- **`rotary`** : `struct_jon_gui_data_rotary`
  ### struct_jon_gui_data_rotary
  - **`platform_azimuth`** : `int32`
  - **`platform_elevation`** : `int32`
  - **`platform_bank`** : `int32`
  - **`use_platform_positioning`** : `int32`
  - **`head_azimuth`** : `int32`
  - **`head_elevation`** : `int32`
  - **`head_bank`** : `int32`
  - **`speed_azimuth`** : `int32`
  - **`speed_elevation`** : `int32`
  - **`speed_bank`** : `int32`
  - **`set_azimuth`** : `int32`
  - **`set_elevation`** : `int32`
  - **`set_speed_azimuth`** : `int32`
  - **`set_speed_elevation`** : `int32`
  - **`set_azimuth_dir`** : `int32`
  - **`set_elevation_dir`** : `int32`
  - **`set_azimuth_offset`** : `int32`
  - **`is_scanning`** : `int32`
  - **`is_scanning_paused`** : `int32`
  - **`scan_target`** : `int32`
  - **`scan_target_max`** : `int32`
  - **`scan_cur_target_azimuth`** : `int32`
  - **`scan_cur_target_elevation`** : `int32`
  - **`scan_cur_target_day_zoom_table_index`** : `int32`
  - **`scan_cur_target_heat_zoom_table_index`** : `int32`
  - **`scan_cur_target_linger`** : `int32`
  - **`scan_cur_target_speed`** : `int32`
  - **`unnamed_1`** : `union_anon_22`
    ### union_anon_22
    - **`device_status`** : `int32`
    - **`device_status_packed`** : `int32`
  - **`unnamed_2`** : `union_anon_23`
    ### union_anon_23
    - **`mode`** : `int32`
    - **`mode_packed`** : `int32`
  - **`meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
  - **`rotary_init`** : `int32`
  - **`pan_init`** : `int32`
  - **`tilt_init`** : `int32`
- **`power`** : `struct_jon_gui_data_power`
  ### struct_jon_gui_data_power
  - **`s0`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s1`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s2`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s3`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s4`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s5`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s6`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`s7`** : `struct_jon_gui_data_power_module_state`
    ### struct_jon_gui_data_power_module_state
    - **`voltage`** : `int32`
    - **`current`** : `int32`
    - **`power`** : `int32`
    - **`is_alarm`** : `int32`
    - **`can_cmd_address`** : `int32`
    - **`can_data_address`** : `int32`
    - **`is_power_on`** : `int32`
    - **`unnamed_1`** : `union_anon_24`
      ### union_anon_24
      - **`can_device`** : `int32`
      - **`can_device_packed`** : `int32`
  - **`meteo`** : `struct_jon_gui_data_component_meteo`
    ### struct_jon_gui_data_component_meteo
    - **`temperature`** : `int32`
    - **`humidity`** : `int32`
    - **`pressure`** : `int32`
- **`cv`** : `struct_jon_gui_data_cv`
  ### struct_jon_gui_data_cv
  - **`af_day_enabled`** : `int32`
  - **`af_heat_enabled`** : `int32`
  - **`tracking_day`** : `int32`
  - **`tracking_heat`** : `int32`
  - **`vampire_mode_enabled`** : `int32`
  - **`stabilization_mode_enabled`** : `int32`
  - **`recognition_mode_enabled`** : `int32`
  - **`dumping`** : `int32`
  - **`tracking_data_day`** : `struct_jon_gui_tracking_quad[10]` [array of 10]
    Array element type:
      ### struct_jon_gui_tracking_quad
      - **`p1`** : `union_jon_gui_tracking_point`
        ### union_jon_gui_tracking_point
        - **`fields`** : `struct_anon_38`
          ### struct_anon_38
          - **`x`** : `uint32`
          - **`y`** : `uint32`
          - **`color_index`** : `uint32`
        - **`packed`** : `uint32`
      - **`p2`** : `union_jon_gui_tracking_point`
        ### union_jon_gui_tracking_point
        - **`fields`** : `struct_anon_38`
          ### struct_anon_38
          - **`x`** : `uint32`
          - **`y`** : `uint32`
          - **`color_index`** : `uint32`
        - **`packed`** : `uint32`
  - **`tracking_data_heat`** : `struct_jon_gui_tracking_quad[10]` [array of 10]
    Array element type:
      ### struct_jon_gui_tracking_quad
      - **`p1`** : `union_jon_gui_tracking_point`
        ### union_jon_gui_tracking_point
        - **`fields`** : `struct_anon_38`
          ### struct_anon_38
          - **`x`** : `uint32`
          - **`y`** : `uint32`
          - **`color_index`** : `uint32`
        - **`packed`** : `uint32`
      - **`p2`** : `union_jon_gui_tracking_point`
        ### union_jon_gui_tracking_point
        - **`fields`** : `struct_anon_38`
          ### struct_anon_38
          - **`x`** : `uint32`
          - **`y`** : `uint32`
          - **`color_index`** : `uint32`
        - **`packed`** : `uint32`
- **`debug`** : `struct_anon_41`
  ### struct_anon_41
  - **`values`** : `int32[20]` [array of 20]
  - **`display_debug`** : `int32`