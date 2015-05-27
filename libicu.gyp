{
	'includes':
	[
		'../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libicu',
			'type': 'none',

			'direct_dependent_settings':
			{
				'include_dirs':
				[
					'include',
				],
			},
			
			'link_settings':
			{
				'conditions':
				[
					[
						'OS == "mac"',
						{
							'libraries':
							[
								'lib/mac/libicudata.a',
								'lib/mac/libicui18n.a',
								'lib/mac/libicuio.a',
								'lib/mac/libicule.a',
								'lib/mac/libiculx.a',
								'lib/mac/libicutu.a',
								'lib/mac/libicuuc.a',
							],
						},
					],
					[
						'OS == "ios"',
						{
							'libraries':
							[
								'lib/ios/$(SDK_NAME)/libicudata.a',
								'lib/ios/$(SDK_NAME)/libicui18n.a',
								'lib/ios/$(SDK_NAME)/libicuio.a',
								'lib/ios/$(SDK_NAME)/libicule.a',
								'lib/ios/$(SDK_NAME)/libiculx.a',
								'lib/ios/$(SDK_NAME)/libicuuc.a',
							],
						},
					],
					[
						'OS == "linux"',
						{
							# Gyp doesn't seem to handle non-absolute paths here properly...
							'library_dirs':
							[
								'<(src_top_dir_abs)/prebuilt/lib/linux/<(target_arch)',
							],
							
							'libraries':
							[
								'-licui18n',
								'-licuio',
								'-licule',
								'-liculx',
								'-licutu',
								'-licuuc',
								'-licudata',
							],
						},
					],
					[
						'OS == "android"',
						{
							# Gyp doesn't seem to handle non-absolute paths here properly...
							'library_dirs':
							[
								'<(src_top_dir_abs)/prebuilt/lib/andoid/<(target_arch)',
							],
							
							'libraries':
							[
								'-licudata',
								'-licui18n',
								'-licuio',
								'-licule',
								'-liculx',
								'-licutu',
								'-licuuc',
							],
						},
					],
					[
						'OS == "win"',
						{
							'library_dirs':
							[
								'lib/win/<(target_arch)'
							],
							
							'libraries':
							[
								'-lsicudt',
								'-lsicuin',
								'-lsicuio',
								'-lsicule',
								'-lsiculx',
								'-lsicutu',
								'-lsicuuc',
							],
						},
					],
				],
			},
		},
	],
}
