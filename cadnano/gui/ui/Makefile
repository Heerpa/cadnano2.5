IMAGES = mainwindow/images/data-svg.png mainwindow/images/data-new_32.png mainwindow/images/data-open_32.png mainwindow/images/data-save_32.png mainwindow/images/part-new-honeycomb.png mainwindow/images/part-new-square.png mainwindow/images/slice-delete-last.png mainwindow/images/slice-move.png mainwindow/images/part-renum.png mainwindow/images/slice-edit.png mainwindow/images/slice-go-last.png mainwindow/images/slice-go-first.png mainwindow/images/add-bases.svg mainwindow/images/remove-bases.svg mainwindow/images/path-insert.png mainwindow/images/path-pen_48.png mainwindow/images/path-paint.png mainwindow/images/path-move.png mainwindow/images/path-skip.png mainwindow/images/path-nick.png mainwindow/images/path-edit.png mainwindow/images/path-pencil.png mainwindow/images/data-export.png mainwindow/images/path-modify.png mainwindow/images/path-addseq.png mainwindow/images/path-autobreak.png mainwindow/images/part-filter-part.png mainwindow/images/part-filter-endpoint.png mainwindow/images/part-filter-xover.png mainwindow/images/part-filter-strand.png mainwindow/images/path-mod.png mainwindow/images/part-new-hpx.png mainwindow/images/part-new-spx.png mainwindow/images/part-new-origami.png mainwindow/images/part-new-dna.png mainwindow/images/part-outliner.png mainwindow/images/part-new-hcpro.png mainwindow/images/part-new-sqpro.png mainwindow/images/part-filter-even.png mainwindow/images/part-filter-odd.png mainwindow/images/part-filter-fwd.png mainwindow/images/part-filter-rev.png mainwindow/images/slice-snap-helix.png mainwindow/images/slice-snap-angles.png mainwindow/images/slice-move-helix.png mainwindow/images/slice-create-helix.png mainwindow/images/slice-new-part.png mainwindow/images/slice-select-helix.png mainwindow/images/grid-circles.png mainwindow/images/grid-points.png mainwindow/images/grid-lines.png mainwindow/images/outliner-eye.svg mainwindow/images/outliner-lock.svg
DIALOGIMAGES = dialogs/images/path-edit_32.png dialogs/images/path-force-xover.png dialogs/images/path-paint_48.png dialogs/images/grid-circles.png dialogs/images/grid-lines.png dialogs/images/grid-points.png


all: mainwindow/ui_mainwindow.py mainwindow/icons_rc.py dialogs/dialogicons_rc.py dialogs/ui_preferences.py dialogs/ui_latticetype.py dialogs/ui_addseq.py dialogs/ui_about.py dialogs/ui_warning.py

mainwindow/icons_rc.py : mainwindow/cadnano.gui.ui.mainwindow.icons.qrc $(IMAGES)
	pyrcc5 -o $@ $<

mainwindow/ui_mainwindow.py : mainwindow/mainwindow.ui
	pyuic5 $< > $@

dialogs/dialogicons_rc.py : dialogs/cadnano.gui.ui.dialogs.dialogicons.qrc $(DIALOGIMAGES)
	pyrcc5 -o $@ $<

dialogs/ui_preferences.py : dialogs/preferences.ui
	pyuic5 $< > $@

dialogs/ui_latticetype.py : dialogs/latticetype.ui
	pyuic5 $< > $@

dialogs/ui_addseq.py : dialogs/addseq.ui
	pyuic5 $< > $@

dialogs/ui_about.py : dialogs/about.ui
	pyuic5 $< > $@

dialogs/ui_warning.py : dialogs/warning.ui
	pyuic5 $< > $@
