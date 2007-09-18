{*****************************************************************************
 *****                                                                   *****
 *****                         USER1.HP7550.PAS                          *****
 *****                                                                   *****
 *****  Serial Plotter Driver for the Hewlitt Packard 7550A pen plotter  *****
 *****                            Version 8                              *****
 *****               David M. Krowitz June 8, 1987.                      *****
 *****                                                                   *****
 *****      Copyright (c) 1987                                           *****
 *****      David M. Krowitz                                             *****
 *****      Massachusetts Institute of Technology                        *****
 *****      Department of Earth, Atmospheric, and Planetary Sciences     *****
 *****************************************************************************
}


MODULE USER1_HP7550;
              


%NOLIST;
%INSERT '/sys/ins/base.ins.pas';
%INSERT '/sys/ins/cal.ins.pas';
%INSERT '/sys/ins/sio.ins.pas';
%INSERT '/sys/ins/streams.ins.pas';
%INSERT '/sys/ins/pad.ins.pas';
%INSERT '/sys/ins/pgm.ins.pas';
%INSERT '/sys/ins/time.ins.pas';
%INSERT '/sys/ins/tone.ins.pas';
%INSERT '/sys/ins/vfmt.ins.pas';
%INSERT 'user1.ins.pas';
%LIST;




CONST

{Program version number - should be same as in file header above}

    version_number = 8;


{Definitions of standard ascii control characters}

    nul = chr(0);       {null character}
    etx = chr(3);       {etx (control-C) character}
    bs  = chr(8);       {backspace (control-H)}
    tab = chr(9);       {tab (control-I)}
    lf  = chr(10);      {line feed (control-J)}
    vt  = chr(11);      {vertical tab (control-K)}
    ff  = chr(12);      {form feed (control-L)}
    cr  = chr(13);      {carriage return (control-M)}
    sub = chr(26);      {sub (control-Z)}
    esc = chr(27);      {escape}
    rs  = chr(30);      {rs}


TYPE

    str1_t =    packed array[1..1] of char;
    str2_t =    packed array[1..2] of char;
    str3_t =    packed array[1..3] of char;
    str4_t =    packed array[1..4] of char;
    str5_t =    packed array[1..5] of char;
    str6_t =    packed array[1..6] of char;
    str7_t =    packed array[1..7] of char;
    str8_t =    packed array[1..8] of char;
    str9_t =    packed array[1..9] of char;
    str10_t =   packed array[1..10] of char;
    str11_t =   packed array[1..11] of char;
    str12_t =   packed array[1..12] of char;
    str13_t =   packed array[1..13] of char;
    str14_t =   packed array[1..14] of char;
    str15_t =   packed array[1..15] of char;
    str16_t =   packed array[1..16] of char;
    str128_t =  packed array[1..128] of char;

    command_buffer_t =  packed array[1..4096] of char;

    user1_$pen_t =      (unknown,
                         empty,
                         paper_pen,
                         roller_ball_pen,
                         drafting_pen,
                         transparency_pen);



VAR

{Definitions of control sequences for the HP7550 plotter}

    init_plotter:       str3_t;         {initialize plotter characteristics}
    reset_plotter:      str9_t;         {reset plotter after finishing a plot}
    set_handshake:      str5_t;         {set handshake mode to Xon-Xoff}
    set_no_echo:        str12_t;        {set no turnaroud delay, no echo terminate char}
    set_pen_speed:      str3_t;         {set pen speed to default value for this carosel}
    set_pen_force:      str3_t;         {set pen force to default value for this carosel}
    new_page:           str3_t;         {eject current page (if plotted on) and load new page}
    unload_page:        str3_t;         {eject current page without loading new one}
    store_pen:          str3_t;         {put pen back into carosel}
    inq_pen_type:       str3_t;         {find out which pen carosel is installed}
    inq_status:         str3_t;         {inquire plotter status to check if auto-feed in enabled from front-panel}
    write_display:      str2_t;         {write following string to front panel display}
    crlf:               str2_t;         {carriage-return, line-feed sequence}



{Defintions of global variables}

    text_flag:          boolean;                {Flags text-mode output being ignored}
    transparent_flag:   boolean;                {Flags transparent-mode output in progress}
    bitmap_flag:        boolean;                {Flags GMF bitmap plot-mode output being ignored}
    output_done_flag:   boolean;                {Flags output of file completed (all output modes)}
    flush_flag:         boolean;                {True if USER1_FLUSH routine called at least once}
    x_plot_size:        pinteger;               {x dimension of GMR vector file being plotted}
    y_plot_size:        pinteger;               {y dimension of GMR vector file being plotted}
    output_mode:        pr_$data_format_t;      {output mode: text, transparent, or bitmap plot}
    stream_id:          stream_$id_t;           {stream id returned by STREAM_$OPEN}
    status:             status_$t;              {status returned by SIO and STREAM calls}
    seek_key:           stream_$SK_t;           {seek_key returned by STREAM calls}
    pen_type_req:       user1_$pen_t;           {type of pens requested by user}
    pen_type_loaded:    user1_$pen_t;           {type of pens currently loaded in plotter}
    font_width:         INTEGER16;              {Width of current font in pixels}
    font_height:        INTEGER16;              {Height of font in pixels (including spacing between lines}
    font_name:          PAD_$STRING_T;          {Pathname of the font file}
    font_name_len:      INTEGER16;              {Length of the pathname}
    num_chars:          pinteger;               {Width of message requesting pen change to be popped up on screen}
    num_lines:          pinteger;               {Height of message requesting pen change to be popped up on screen}





PROCEDURE USER1_INIT (
                IN  sio_line: integer;
                IN  sio_speed: UNIV sio_$value_t
                );

VAR

    sioname:    array[1..3] of str9_t;      {names of SIO lines for STREAM_$OPEN call}
    i,j:        pinteger;                   {counters}

    BEGIN


        {Identify ourselves.}

        WRITELN ('This is the HP7550-A Plotter Server - Version ',version_number:-1,'.');
        WRITELN;


        {Open I/O stream and set SIO line characteristics}

        sioname[1] := '/dev/sio1';
        sioname[2] := '/dev/sio2';
        sioname[3] := '/dev/sio3';

        stream_$open (sioname[sio_line],9,stream_$append,stream_$no_conc_write,stream_id,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not open output stream: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$speed,sio_speed,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$SPEED: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$nlc_delay,0,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$NLC_DELAY to 0: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$input_sync,true,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$INPUT_SYNC on: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$host_sync,true,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$HOST_SYNC on: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$no_echo,true,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$NO_ECHO on: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$cts_enable,false,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$CTS_ENABLE off: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$quit_enable,false,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$QUIT_ENABLE off: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$parity,sio_$no_parity,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$PARITY to none: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$bits_per_char,sio_$8bpc,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$BPC to 8 bits/char: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;

        SIO_$CONTROL (stream_id,sio_$stop_bits,sio_$stop_1,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** USER1_INIT: Error - could not set SIO_$STOP to 1 stop bit: ',
                     sioname[sio_line],' ****');
            PGM_$EXIT;
        END;


        {Initialize strings of control characters for printer}

        init_plotter[1] := 'I';
        init_plotter[2] := 'N';
        init_plotter[3] := ';';

        reset_plotter[1] := 'R';
        reset_plotter[2] := 'O';
        reset_plotter[3] := ';';
        reset_plotter[4] := 'I';
        reset_plotter[5] := 'P';
        reset_plotter[6] := ';';
        reset_plotter[7] := 'D';
        reset_plotter[8] := 'F';
        reset_plotter[9] := ';';

        set_handshake[1] := esc;
        set_handshake[2] := '.';
        set_handshake[3] := 'P';
        set_handshake[4] := '1';
        set_handshake[5] := ':';

        set_no_echo[1]  := esc;
        set_no_echo[2]  := '.';
        set_no_echo[3]  := 'M';
        set_no_echo[4]  := '0';
        set_no_echo[5]  := ';';
        set_no_echo[6]  := '0';
        set_no_echo[7]  := ';';
        set_no_echo[8]  := '0';
        set_no_echo[9]  := ';';
        set_no_echo[10] := '1';
        set_no_echo[11] := '3';
        set_no_echo[12] := ':';
                      
        set_pen_speed[1] := 'V';
        set_pen_speed[2] := 'S';
        set_pen_speed[3] := ';';
                      
        set_pen_force[1] := 'F';
        set_pen_force[2] := 'S';
        set_pen_force[3] := ';';

        new_page[1] := 'P';
        new_page[2] := 'G';
        new_page[3] := ';';

        unload_page[1] := 'N';
        unload_page[2] := 'R';
        unload_page[3] := ';';

        store_pen[1] := 'S';
        store_pen[2] := 'P';
        store_pen[3] := ';';

        inq_pen_type[1] := 'O';
        inq_pen_type[2] := 'T';
        inq_pen_type[3] := ';';

        inq_status[1] := esc;
        inq_status[2] := '.';
        inq_status[3] := 'O';

        write_display[1] := 'W';
        write_display[2] := 'D';

        crlf[1] := cr;
        crlf[2] := lf;


        {Initialize output-mode flags}

        text_flag := false;
        transparent_flag := false;
        bitmap_flag := false;
        output_done_flag := true;
        flush_flag := false;


        {Initialize the printer settings}

        STREAM_$PUT_CHR (stream_id,ADDR(init_plotter),3,seek_key,status);
        STREAM_$PUT_CHR (stream_id,ADDR(set_handshake),5,seek_key,status);
        STREAM_$PUT_CHR (stream_id,ADDR(set_no_echo),12,seek_key,status);
        STREAM_$PUT_CHR (stream_id,ADDR(store_pen),3,seek_key,status);
        output_mode := pr_$transparent;

    END; {End of USER1_INIT}





PROCEDURE USER1_WRITE (
                IN  buffer: UNIV pr_$buf_t;
                IN  buffer_length: pinteger
                );




    PROCEDURE USER1_WRITE_TEXT (
                    IN  buffer: UNIV pr_$buf_t;
                    IN  buffer_length: pinteger
                    );

        BEGIN

            {If USER1_FLUSH has not been called at least once after the end
             of some text-mode output then ignore the output -- it is the
             printer configuration info which is printed when PRSVR starts
             up. It is not legal plotter output, but we don't want to print
             an error message for it since it is not an error on the part of
             the user -- PRSVR always prints its configuration on startup.}

            IF flush_flag = TRUE THEN BEGIN
                IF (text_flag = FALSE) AND (output_done_flag = TRUE) THEN BEGIN
                    WRITELN ('Text mode output not possible on plotter - file discarded');
                END;
            END;
            text_flag := TRUE;
            output_done_flag := FALSE;
        END; {End of USER1_WRITE_TEXT}



    PROCEDURE USER1_WRITE_TRANSPARENT (
                    IN  buffer: UNIV pr_$buf_t;
                    IN  buffer_length: pinteger
                    );

        BEGIN

            IF (transparent_flag = FALSE) THEN BEGIN
                WRITELN ('Sending TRANSPARENT mode output to plotter');
            END;
            STREAM_$PUT_CHR (stream_id,ADDR(buffer),buffer_length,seek_key,status);
            transparent_flag := TRUE;
            output_done_flag := FALSE;
        END; {End of USER1_WRITE_TRANSPARENT}



    PROCEDURE USER1_WRITE_PLOT (
                    IN  buffer: UNIV pr_$buf_t;
                    IN  buffer_length: pinteger
                    );  

        BEGIN
            IF (bitmap_flag = FALSE) AND (output_done_flag = TRUE) THEN BEGIN
                WRITELN ('GMF bitmap mode output not possible on plotter - file discarded');
            END;
            bitmap_flag := TRUE;
            output_done_flag := FALSE;
        END; {End of USER1_WRITE_PLOT}


    BEGIN       {Beginning of actual USER1_WRITE code}

        {Determine printer mode and dispatch for output of buffer}

        CASE output_mode OF
            pr_$text:           user1_write_text (buffer,buffer_length);
            pr_$transparent:    user1_write_transparent (buffer,buffer_length);
            pr_$plot:           user1_write_plot (buffer,buffer_length)
        END;

    END; {End of USER1_WRITE}




PROCEDURE GET_PEN_TYPE (
                        OUT pen_type_loaded:    user1_$pen_t
                        );

VAR

    i,j:            pinteger;               {counters}
    count:          pinteger;               {number of fields decoded by VFMT_$RS}
    pen_type:       integer16;              {pen carosel type number}
    pen_map:        integer16;              {pen stall map (which pens are in carosel)}
    sleep:          TIME_$CLOCK_T;          {number of seconds to sleep before re-checking pen type}


    BEGIN

        {Request pen carosel type from plotter.
         If pen carosel installed is empty, sleep 5 seconds and
         then try again until the user loads the pens.}

        REPEAT

            STREAM_$PUT_CHR (stream_id,ADDR(inq_pen_type),3,seek_key,status);
            CAL_$SEC_TO_CLOCK (2,sleep);
            TIME_$WAIT (TIME_$RELATIVE,sleep,status);
            VFMT_$RS5 (stream_id,'%ESWD%ESWD%$',count,status,pen_type,pen_map,i,j,0);
            IF (status.all <> STATUS_$OK) THEN BEGIN
                WRITELN ('**** GET_PEN_TYPE: Error - could not read plotter pen type ****');
                PGM_$EXIT;
            END;

            CASE pen_type OF
                -1:     pen_type_loaded := unknown;
                 0:     pen_type_loaded := empty;
                 1:     pen_type_loaded := paper_pen;
                 2:     pen_type_loaded := roller_ball_pen;
                 3:     pen_type_loaded := drafting_pen;
                 4:     pen_type_loaded := transparency_pen;
            END;

            IF (pen_type_loaded = empty) THEN BEGIN
                CAL_$SEC_TO_CLOCK (5,sleep);
                TIME_$WAIT (TIME_$RELATIVE,sleep,status);
                IF (status.all <> STATUS_$OK) THEN BEGIN
                    WRITELN ('**** GET_PEN_TYPE: Error - sleep call failed ****');
                    PGM_$EXIT;
                END;
            END;

        UNTIL (pen_type_loaded <> empty);

    END;    {End of GET_PEN_TYPE}




FUNCTION INQ_AUTO_FEED: BOOLEAN;

VAR

    i,j:            pinteger;               {counters}
    count:          pinteger;               {number of fields decoded by VFMT_$RS}


    BEGIN

        {Find out the the plotter's auto-feed is enabled from the front panel.
         Get the plotter's status word. Bit 0 (low order bit) of the status
         word is 1 if auto-feed is enabled and 0 otherwise.}

        STREAM_$PUT_CHR (stream_id,ADDR(inq_status),3,seek_key,status);
        VFMT_$RS2 (stream_id,'%EUWD%$',count,status,i,0);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** INQ_AUTO_FEED: Error - could not read plotter status ****');
            PGM_$EXIT;
        END;

        IF (i&1 = 0) THEN BEGIN
            INQ_AUTO_FEED := FALSE
        END
        ELSE BEGIN
            INQ_AUTO_FEED := TRUE;
        END;

    END;    {End of INQ_AUTO_FEED}




PROCEDURE REQUEST_PENS (
                        IN  pen_type_needed:    user1_$pen_t
                        );

VAR

    i,j:                pinteger;               {counters}
    pen_type_loaded:    user1_$pen_t;           {kind of pens currently loaded in plotter}
    sleep:              TIME_$CLOCK_T;          {number of seconds to sleep before re-checking pen type}
    pad_stream_id:      STREAM_$ID_T;           {Stream ID number of transcript pad}
    pad_seek_key:       STREAM_$SK_T;           {Stream's seek-key}
    pad_lines:          INTEGER16;              {Number of lines in the message window}
    pad_window:         PAD_$WINDOW_DESC_T;     {Position and size of the message window}
    beep_time:          TIME_$CLOCK_T;          {Length of time to beep at user}



    BEGIN

        {Request the desired pens to be loaded by the user.
         Write a request to the front panel display of the HP7550 and also
         pop up a windown on the node running the plotter server to
         request the new pens to be loaded. Then unload the current page
         so that the user will be sure to load the correct paper as
         well as the correct pens.}


        {Write message to front panel LCD display.
         Check if auto-feed is enabled so we can display correct status
         in the message so that the user will do the 'right stuff'.}

        STREAM_$PUT_CHR (stream_id,ADDR(write_display),2,seek_key,status);
        IF (inq_auto_feed = FALSE) THEN BEGIN
            STREAM_$PUT_CHR (stream_id,ADDR('  '),2,seek_key,status);
        END
        ELSE BEGIN
            STREAM_$PUT_CHR (stream_id,ADDR('* '),2,seek_key,status);
        END;
        CASE pen_type_needed OF
            transparency_pen:   STREAM_$PUT_CHR (stream_id,ADDR('PLEASE LOAD   TRANSPARENCY 
PEN'),30,seek_key,status);
            paper_pen:          STREAM_$PUT_CHR (stream_id,ADDR('PLEASE LOAD   PAPER PENS      
'),30,seek_key,status);
            drafting_pen:       STREAM_$PUT_CHR (stream_id,ADDR('PLEASE LOAD   DRAFTING PENS   
'),30,seek_key,status);
        END;
        STREAM_$PUT_CHR (stream_id,ADDR(etx),1,seek_key,status);


        {Pop up a window on the node running the plotter server
         and request the pens to be changed.}

        pad_window.top := 0;
        pad_window.left := 0;
        pad_window.height := 100;
        pad_window.width := 400;
        PAD_$CREATE_WINDOW ('',0,PAD_$TRANSCRIPT,1,pad_window,pad_stream_id,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('***** REQUEST_PENS: Error - PAD_$CREATE_WINDOW call failed *****');
            PGM_$EXIT;
        END;



        {Write out the message.}

        num_chars := 47;
        num_lines := 5;
        STREAM_$PUT_REC 
(pad_stream_id,ADDR('***********************************************'),num_chars,pad_seek_key,status);
        STREAM_$PUT_REC (pad_stream_id,ADDR(crlf),2,pad_seek_key,status);
        STREAM_$PUT_REC (pad_stream_id,ADDR(crlf),2,pad_seek_key,status);
        CASE pen_type_needed OF
            transparency_pen:   STREAM_$PUT_REC (pad_stream_id,ADDR('Please load transparency pens in HP7550 
plotter'),num_chars,pad_seek_key,status);
            paper_pen:          STREAM_$PUT_REC (pad_stream_id,ADDR('    Please load paper pens in HP7550 
plotter   '),num_chars,pad_seek_key,status);
            drafting_pen:       STREAM_$PUT_REC (pad_stream_id,ADDR('  Please load drafting pens in HP7550 
plotter  '),num_chars,pad_seek_key,status);
        END;
        STREAM_$PUT_REC (pad_stream_id,ADDR(crlf),2,pad_seek_key,status);
        STREAM_$PUT_REC (pad_stream_id,ADDR(crlf),2,pad_seek_key,status);
        STREAM_$PUT_REC 
(pad_stream_id,ADDR('***********************************************'),num_chars,pad_seek_key,status);
        STREAM_$PUT_REC (pad_stream_id,ADDR(crlf),2,pad_seek_key,status);



        {Resize window to fit the message.}

        PAD_$INQ_FONT (pad_stream_id,font_width,font_height,font_name,256,font_name_len,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('***** REQUEST_PENS: Error - PAD_$INQ_FONT call failed *****');
            PGM_$EXIT;
        END;
        pad_window.width := (num_chars+2)*font_width;
        pad_window.height := (num_lines+2)*font_height;
        PAD_$SET_FULL_WINDOW (pad_stream_id,1,pad_window,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('***** REQUEST_PENS: Error - PAD_$SET_FULL call failed *****');
            PGM_$EXIT;
        END;


        {Beep at the user to get their attention.}

        beep_time.high16 := 0;
        beep_time.low32  := 30000;
        TONE_$TIME (beep_time);


        {Wait until the correct pens are loaded. If the user loads some
         pens and they are still the wrong type, then unload the paper
         again and keep waiting.}

        get_pen_type (pen_type_loaded);
        WHILE (pen_type_loaded <> pen_type_needed) DO BEGIN
            STREAM_$PUT_CHR (stream_id,ADDR(unload_page),3,seek_key,status);
            CAL_$SEC_TO_CLOCK (5,sleep);
            TIME_$WAIT (TIME_$RELATIVE,sleep,status);
            IF (status.all <> STATUS_$OK) THEN BEGIN
                WRITELN ('**** REQUEST_PENS: Error - sleep call failed ****');
                PGM_$EXIT;
            END;
            get_pen_type (pen_type_loaded);
        END;

    
        {Reset the front panel display and close the window we popped
         up on the node running the plotter server. Window will close
         automatically when the pad-stream is closed.}

        STREAM_$PUT_CHR (stream_id,ADDR(write_display),2,seek_key,status);
        STREAM_$PUT_CHR (stream_id,ADDR(etx),1,seek_key,status);

        PAD_$SET_AUTO_CLOSE (pad_stream_id,1,TRUE,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('***** REQUEST_PENS: Error - PAD_$SET_AUTO_CLOSE call failed *****');
            PGM_$EXIT;
        END;
        STREAM_$DELETE (pad_stream_id,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('***** REQUEST_PENS: Error - PAD_$CLOSE call failed *****');
            PGM_$EXIT;
        END;


        {Set the pen speed and pen force to the default values for this new
         carosel. Then wait 20 seconds to allow the user to reset the speed
         and force to non-standard values if they wish.}

        STREAM_$PUT_CHR (stream_id,ADDR(set_pen_speed),3,seek_key,status);
        STREAM_$PUT_CHR (stream_id,ADDR(set_pen_force),3,seek_key,status);
        CAL_$SEC_TO_CLOCK (20,sleep);
        TIME_$WAIT (TIME_$RELATIVE,sleep,status);
        IF (status.all <> STATUS_$OK) THEN BEGIN
            WRITELN ('**** REQUEST_PENS: Error - sleep call failed after setting pen speed/force ****');
            PGM_$EXIT;
        END;



    END;    {End of REQUEST_PENS}




PROCEDURE USER1_SET_MODE (
                IN  mode: pr_$set_op_t;
                IN  data: pr_$data_rec_t
                );



    {Start of main body of USER1_SET_MODE.}

    BEGIN

      CASE mode OF
        pr_$font_weight:      BEGIN
                                CASE data.font_weight OF
                                  pr_$light:        pen_type_req := transparency_pen;
                                  pr_$medium:       pen_type_req := paper_pen;
                                  pr_$bold:         pen_type_req := drafting_pen;
                                END;
                                get_pen_type (pen_type_loaded);
                                IF (pen_type_req <> pen_type_loaded) AND (flush_flag = TRUE) THEN BEGIN
                                  request_pens (pen_type_req);
                                END;
                              END;
        pr_$font_size:        ;
        pr_$text_precision:   ;
        pr_$data_format:      output_mode := data.data_format;
        pr_$pitch:            ;
        pr_$x_dimension:      ;
        pr_$y_dimension:      ;
        pr_$rep_factor:       ;
        pr_$config:           ;
        pr_$copies:           ;
        pr_$server_db:        WITH data.server_db_ptr^ DO BEGIN
                                output_mode := print_mode;
                                CASE weight OF
                                  pr_$light:        pen_type_req := transparency_pen;
                                  pr_$medium:       pen_type_req := paper_pen;
                                  pr_$bold:         pen_type_req := drafting_pen;
                                END;
                                get_pen_type (pen_type_loaded);
                                IF (pen_type_req <> pen_type_loaded) AND (flush_flag = TRUE) THEN BEGIN
                                  request_pens (pen_type_req);
                                END;
                              END;
      END;

    END; {End of USER1_SET_MODE}




PROCEDURE USER1_RETURN_INFO (
                IN  query: pr_$inq_op_t;
                OUT  data: pr_$data_rec_t
                );

    BEGIN

        CASE query OF
            pr_$bpi:                     BEGIN
                                            data.bpi.x := 1016;
                                            data.bpi.y := 1016;
                                        END;
            pr_$rep_ability:            data.rep_ability := true;
            pr_$driver_db:              WITH data.driver_db_ptr^ DO BEGIN
                                            valid := TRUE;
                                            copies := FALSE;
                                            color_format := none;
                                            bw_rev := FALSE;
                                            image_rotation := FALSE;
                                        END;
        END;

    END; {End of USER1_RETURN_INFO}





PROCEDURE USER1_FLUSH;

    BEGIN                        

        {Reset output-mode flags, eject the current page if it has been plotted on,
         and load a new piece of paper into the plotter (assuming auto-feed is on
         and paper tray has not empty - otherwise plotter will wait for new paper
         to be loaded). }

        IF transparent_flag = true THEN BEGIN
            STREAM_$PUT_CHR (stream_id,ADDR(reset_plotter),9,seek_key,status);
            STREAM_$PUT_CHR (stream_id,ADDR(store_pen),3,seek_key,status);
            STREAM_$PUT_CHR (stream_id,ADDR(new_page),3,seek_key,status);
        END;

        {We have just finished output of some file (or just finished discarding
         it) so we set flag to inhibit printing of error message when PRSVR
         tries to send a form-feed in text-mode to move printer (plotter) to
         a new piece of paper.}

        IF (text_flag = true) THEN BEGIN
            output_done_flag := true;
        END;

        {IF USER1_FLUSH has been called at least once after performing some
         text-mode output then transparent-mode output can be enabled
         (first time around the output is the PRSVR configuration info
         which is printed the program is started -- but the output is not
         HP-GL commands so we quietly throw it away). All output modes have
         been completed so we reset their flags.}

        IF (text_flag = TRUE) THEN BEGIN
            flush_flag := true;             {enable transparent-mode output}
        END;
        text_flag := false;
        transparent_flag := false;
        bitmap_flag := false;

    END; {End of USER1_FLUSH}





PROCEDURE USER1_CLOSE;

    BEGIN

        STREAM_$CLOSE (stream_id,status);

    END; {End of USER1_CLOSE}





{***** End of module USER1_HP7550 *****}

