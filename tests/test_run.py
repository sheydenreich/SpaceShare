from SpaceShare import run_spaceshare

def test_dry_run():
    run_spaceshare(config_file="test.cfg",dry_run=True, 
                test_login=False, confirm_groups=False)
    
test_dry_run()